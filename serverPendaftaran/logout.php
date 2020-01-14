<?php
if (isset($_GET['submit'])){
    session_start();
    session_unset();
    session_destroy();
    header("Location: ../serverPendaftaran/index.php");
    exit();
}
?>