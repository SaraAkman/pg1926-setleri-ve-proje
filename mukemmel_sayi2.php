<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>

<body>
<?php
$_girilen_sayi=$_POST['sayi'];

$b=0;

    for($i=1;$i<=1000;$i=$i+1)
   {
    $c=(pow(2,$i)-1)*(pow(2,($i-1)));
    
    if($c==$_girilen_sayi)
       
        $b++;
     
   }
    
if($b>0)
    echo "\n Girilen sayı mükemmel sayıdır.";
else
    echo "\n Girilen sayı mükemmel sayı değildir.\n ";





?>




<A HREF="javascript:javascript:history.go(-1)">Tekrar denemek için buraya tıklayınız!</A>
<br />
</body>
</html>

