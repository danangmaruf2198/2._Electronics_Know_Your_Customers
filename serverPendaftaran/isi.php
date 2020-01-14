<?php
$kondisi = true;
$hashedPw=0;
//koneksi database
$db = mysqli_connect("localhost","root","","bank") or die ("GABISA CONNECT");
$query = mysqli_query($db,"SELECT * FROM biodata");
$lihat = mysqli_fetch_array($query);
//=========
$nama=mysqli_real_escape_string($db,$_GET['nama']);
$nohp=mysqli_real_escape_string($db,$_GET['nohp']);
$email=mysqli_real_escape_string($db,$_GET['email']);
$pw=mysqli_real_escape_string($db,$_GET['pw']);
$jenisKelamin=mysqli_real_escape_string($db,$_GET['jenisKelamin']);
$pekerjaan=mysqli_real_escape_string($db,$_GET['pekerjaan']);
$goldar=mysqli_real_escape_string($db,$_GET['goldar']);
$gaji=mysqli_real_escape_string($db,$_GET['gaji']);   
$noktp=mysqli_real_escape_string($db,$_GET['noktp']);

//error handler untuk data yang sama
function dataSama($lihat,$kondisi,$query){
    while($lihat = mysqli_fetch_array($query))
    {
        if($lihat['noktp'] == $GLOBALS['noktp'] || $lihat['email'] == $GLOBALS['email'] ||$lihat['nohp'] == $GLOBALS['nohp'])
        {
            $GLOBALS ['kondisi'] = false;
        }
    }
    if($GLOBALS ['kondisi'] == false)
    {// bikin json untuk respon noktp sudah ada
    echo '<script language="javascript">';
            echo 'alert("data ktp atau noktp atau email sudah terdaftar")';
            echo '</script>';
            echo '<a href="http://localhost/ekyc/serverPendaftaran/">KEMBALI</a> ';
    }
}
function checkData($nama,$nohp,$email,$pw,$jenisKelamin,$pekerjaan,$goldar,$gaji,$noktp,$lihat,$kondisi,$query){
    if (empty($nama)||empty($nohp)||empty($email)||empty($pw)||empty($jenisKelamin)||empty($pekerjaan)||empty($goldar)||empty($gaji)||empty($noktp)){
        header("Location : ../signup.php?signup=empty");
        //bikin json untuk indikator data kurang
        exit();
    }else{
        //error handler character
        if (!preg_match("/^[a-zA-Z]*$/",$nama)|| !preg_match("/^[a-zA-Z]*$/",$pekerjaan)) {
            header("Location: ../signup.php?signup=wrongCharacter");
            exit();
            //bikin json untuk indikator input character salah
        }else{
            //error handle check email valid
            if(!filter_var($email, FILTER_VALIDATE_EMAIL)){
                header("Location: ../signup.php?signup=emailNotValid");
                exit();
            }else{
                //check username sama dan ID sama
                dataSama($lihat,$kondisi,$query);
                //hashing the password
                $GLOBALS ['hashedPw']= password_hash($pw, PASSWORD_DEFAULT);
                $GLOBALS ['kondisi']=true;               
            }
        } 
    }
}
//error=0 dan data benar semua
checkData($nama,$nohp,$email,$pw,$jenisKelamin,$pekerjaan,$goldar,$gaji,$noktp,$lihat,$kondisi,$query);

if(isset($_GET['nama']) && $kondisi == true)
{
    mysqli_query($db,"INSERT INTO biodata (nama,nohp,email,pw,jenisKelamin,pekerjaan,goldar,gaji,noktp) VALUES ('$_GET[nama]','$_GET[nohp]','$_GET[email]','$hashedPw','$_GET[jenisKelamin]','$_GET[pekerjaan]','$_GET[goldar]','$_GET[gaji]','$_GET[noktp]' )");
    header("Location:http://localhost/ekyc/serverPendaftaran/");
}





?>