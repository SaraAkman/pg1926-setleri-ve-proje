<?php

date_default_timezone_set('Europe/Istanbul');

$saat = date("H");

$sabah = "06";
$ogle  = "10";
$ikindi = "17";
$aksam = "20";
$yatsi= "00";

if($saat >= $sabah AND $saat < $ogle)
{
    echo "Günaydın";
}

else if($saat >= $ogle AND $saat < $ikindi)
{
    echo "İyi Günler";
}

else if($saat >= $ikindi AND $saat < $aksam)
{
    echo "İyi Akşamlar";
}

else if($saat >= $aksam && $saat < $yatsi)
{
    echo "İyi Geceler";
}

else
{
    echo "Esenlikler Dilerim";
}

?> 

