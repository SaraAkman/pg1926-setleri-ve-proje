<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>

<body>
<?php
$_girilen_sayi=$_POST['sayi'];

$asalsayi=0; $i=2;

do
{
    if ($_girilen_sayi % $i == 0)
    {
        $asalsayi = 1;
    }
    $i++;
}
while($i<$_girilen_sayi);

if ($asalsayi != 1)
{
    $hesap="Girdiğiniz sayı asal bir sayıdır!";
}
else
{
    $hesap="Girdiğiniz sayı asal bir sayı değildir!";
}

?>

    <td width="206">Girdiğiniz sayı buydu:</td>
    <td width="213"><?php echo $_girilen_sayi; ?></td>
 

    
<h3><?php echo $hesap; ?>  </h3>
 
    
    </td>

<A HREF="javascript:javascript:history.go(-1)">Tekrar denemek için buraya tıklayınız!</A>
<br />

</body>
</html>


