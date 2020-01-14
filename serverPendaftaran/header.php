<?php
session_start();
?>

<html>
<head> 
    <link rel="stylesheet" type="text/css" href="style.css"
</head>
<body>
<header>
    <nav>
        <div class="main-wrapper">
            <ul>
                <li><a href="index.php">HOME</a></li>
            </ul>
            <div class="nav-login">
                <?php
                if (isset($_SESSION['email'])){
                    echo '<form action="logout.php" methode="GET">';
                    echo 'Login as= '.$_SESSION['email'].'<br>';
                    echo '<button type="submit" name="submit">logout</button>
                          </form>';
                }else{
                    echo '<form action="login.php" methode="GET">
                    <input type="text" name="email" placeholder="Username/ID mu">
                    <input type="password" name="pw" placeholder="Password mu">
                    <button type="submit" name="submit">LOGIN</button>
                    </form>
                    <a href="signup.php">Daftar</a>';
                }
                ?>                
            </div>
        </div>
    </nav>
</header>
