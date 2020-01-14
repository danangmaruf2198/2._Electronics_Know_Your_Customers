<?php
session_start();

if (isset($_GET['submit'])){
    $db = mysqli_connect("localhost","root","","bank") or die ("GABISA CONNECT");
    $db1 = mysqli_query($db,"SELECT * FROM biodata");
    $db2 = mysqli_query($db,"SELECT * FROM dataGambar");
    
    //scanning satu satu pake double while
    function pencocokan($db,$db1,$db2){
        while($biodata = mysqli_fetch_assoc($db1)){
            echo $biodata['email'];    
            echo "<br>";
            $db2 = mysqli_query($db,"SELECT * FROM dataGambar");
            while($dataGambar = mysqli_fetch_assoc($db2)){
               // echo $dataGambar['email']."<br>";
                if($biodata['email']==$dataGambar['email']){
                    echo"data sama <br>";
                    $kondisi=false;
                    break;
                }else{
                    echo "data beda<br>";
                    $kondisi=true;
                }
            }
            if($kondisi==true){
                echo "insert baru <br>";
                $emailBaru=$biodata['email'];
                echo $emailBaru."<br>";
                mysqli_query($db,"INSERT INTO dataGambar (gambar,email,keadaan) VALUES ('','$emailBaru','')");
            }else{
                echo "data sama <br>";
            }
            
        }
    }
    pencocokan($db,$db1,$db2);
    
    $email=mysqli_real_escape_string($db,$_GET['email']);
    $pw=mysqli_real_escape_string($db,$_GET['pw']);

    //error handler
    // misal input kosong
    if(empty($email)||empty($pw)){
        header("Location: ../index.php?login=empty");
        exit();
    }else{
        $sql= "SELECT * FROM biodata WHERE email='$email'";
        $result=mysqli_query($db,$sql);
        $resultCheck=mysqli_num_rows($result);
        
        if($resultCheck<1){
            header("Location: ../index.php?login=notMatch");
            exit();
        }
        else{
            if($row=mysqli_fetch_assoc($result)){
                //de-hashing password and matching
                $hashedPwCheck= password_verify($pw,$row['pw']);
                if($hashedPwCheck== false){
                    header("Location: ../index.php?login=notMatch");
                    exit();
                } elseif($hashedPwCheck== true){
                    // logined user
                    $_SESSION['email']= $row['email'];
                    $_SESSION['noktp']= $row['noktp'];
                    $_SESSION['nohp']= $row['nohp'];
                    
                    header("Location: ../serverPendaftaran/index.php?login=Sucess");
                    exit();
                }
            }
        }
    }
} 
else {
    header("Location: ../index.php?login=error");
    exit();
}



?>