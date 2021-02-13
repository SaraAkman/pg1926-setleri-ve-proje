var oynatma_butonu;
var muzik_adi;
var sarkici;
var rngctrl;
var tts;
var bitis_zamani;
var app;
var body;
var thumbnail;

var grads = ["rgb(166, 7, 7), rgb(33, 16, 16)", "rgb(86, 76, 113), rgb(24, 23, 26)", "rgb(55, 86, 108), rgb(21, 24, 26)"];

var songs = [
    { id: 1, muzik_adi: "Castle On The Hill", artist: "Ed Sheeran", link: "https://dl.dropbox.com/s/18gwex5w964mumb/Ed%20Sheeran%20-%20Castle%20On%20The%20Hill%20%5BOfficial%20Lyric%20Vi?raw=1", length: 289, lenS: "4:49", thumbnail: "https://dl.dropbox.com/s/rnxhi0gbelzg0pu/Castle_On_The_Hill_%28Official_Single_Cover%29_by_Ed_Sheeran.png?raw=1" },

    { id: 2, muzik_adi: "I don\'t care", artist: "Ed Sheeran & Justin bieber", link: "https://dl.dropbox.com/s/fnoiqhzufw3pgrt/Ed%20Sheeran%20%26%20Justin%20Bieber%20-%20I%20Don%27t%20Care%20%5BOfficia?raw=1", length: 217, lenS: "3:37", thumbnail: "https://dl.dropbox.com/s/bdmk8xqm3xfukay/220px-Ed_Sheeran_%26_Justin_Bieber_-_I_Don%27t_Care.png?raw=1" },

    { id: 3, muzik_adi: "On My Way", artist: "Alan Walker", link: "https://dl.dropbox.com/s/ftw563vngoy2u97/Alan%20Walker%2C%20Sabrina%20Carpenter%20%26%20Farruko%20%20-%20On%20My?raw=1", length: 217, lenS: "3:37", thumbnail: "https://dl.dropbox.com/s/xpk3miy7cw046mh/images%20%283%29.jpeg?raw=1" }
];

var isPlaying = false;
var songIndex = 0;

var playSong;

var liked = false;

window.onload = () => {
    body = document.getElementById("body");
    var loader = document.getElementById("loader");
    app = document.getElementById("app");
    thumbnail = document.getElementById("thumbnail");
    setTimeout(() => {
        loader.style.display = "none";
        app.style.display = "block";
    }, 2000);

    tts = songs.length;
    //alert(tts);

    oynatma_butonu = document.getElementById("play");
    muzik_adi = document.getElementById("song-name");
    sarkici = document.getElementById("artist-name");
    bitis_zamani = document.getElementById("end");
    rngctrl = document.getElementById("range-controls");
    muzik_adi.innerText = songs[songIndex].muzik_adi;
    sarkici.innerText = songs[songIndex].artist;
    bitis_zamani.innerText = songs[songIndex].lenS;
    thumbnail.src = songs[songIndex].thumbnail;

    alert("İnternet bağlantınızın olduğunu düşünüyorsanız Tamam'a basın.");
}

const setGrad = () => {
    var r = Math.floor(Math.random() * grads.length);
    body.style.backgroundImage = "linear-gradient(" + grads[r] + ")";
}

const credits = () => {
    alert("1)Sara Akman ve Muhammed Çiçek oluşturmuştur.\n2)Simgeler Font-awesome'dan\n3)Spotify'ı buradan indirebilirsiniz: https://play.google.com/store/apps/details?id=com.spotify.music");
}

const like = () => {
    var likebtn = document.getElementById("like");
    liked = (!liked);
    (liked) ? likebtn.style.color = "green": likebtn.style.color = "white";
}

const play = () => {
    //alert("Play feature coming soon");
    if (!isPlaying) {
        playSong = new Audio();
        playSong.src = songs[songIndex].link;
        playSong.play();

        isPlaying = true;
        oynatma_butonu.className = "fas fa-pause";
    } else {
        playSong.pause();
        isPlaying = false;
        oynatma_butonu.className = "fa  fa-caret-right";
    }
    muzik_adi.innerText = songs[songIndex].muzik_adi;
    sarkici.innerText = songs[songIndex].artist;
    bitis_zamani.innerText = songs[songIndex].lenS;
    thumbnail.src = songs[songIndex].thumbnail;
}

const next = () => {
    //alert("Next feature coming soon");
    if (isPlaying) {
        playSong.pause();
        isPlaying = false;
    }
    if (songIndex < tts - 1) {
        songIndex++;
        //console.log("inc");
    } else {
        songIndex = 0;
        //console.log("zero");
    }
    setGrad();
    //console.log(songIndex);
    play();
}

const prev = () => {
    //alert("Prev feature coming soon");
    if (isPlaying) {
        playSong.pause();
        isPlaying = false;
    }
    if (songIndex > 0) { songIndex-- };
    setGrad();
    play();
}

const download = () => {
    alert("Cihaz desteklenmiyor");
}
