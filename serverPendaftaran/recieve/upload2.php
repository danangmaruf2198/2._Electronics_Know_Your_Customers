<?php

if (isset($_POST['submit'])){
    echo "lala<br>";
    $file = $_FILES['file'];
    print_r($file);
    $fileName=$_FILES['file']['name'];
    /*
    $fileTmpName=$_FILES['file']['tmp_name'];
    $fileSize=$_FILES['file']['size'];
    $fileError=$_FILES['file']['error'];
    $fileType=$_FILES['file']['type'];

    $fileExt= explode('.',$fileName);
    $fileActualExt= strlower(end($fileExt));
    $allowed= array('jpg','jpeg','png','pdf');
    
    if (in_array($fileActualExt,$allowed)) {
        if($fileError==0){
            if (filesize<5000){ //5000 equal then 5MB
                 $fileNameNew= uniqid('',true).".".$fileActualExt;
                 $fileDestenation='../'.$fileNameNew;
                 move_uploaded_file($fileTmpName,$fileDestenation);
                 mysqli_query($db,"INSERT INTO dataGambar (gambar,email,keadaan) VALUES ('','$emailBaru','')");
                 header("Location: ../index.php?uploadSuccess");
                 exit();
            }else{
                echo "your file is too big";
            }
        }else{
            echo "There is an error in your image";
        }
    }else {
        echo "you can't upload this file type!";
    }*/
}else {
    echo "error file image";
}

//bikin dashboard active account yang belum di log out dan dijadiin satu sama gambar 
//pake method UPDATE jadi harus insert semua data ke db image
?>