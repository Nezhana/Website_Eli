var $ = jQuery.noConflict();
$(document).ready((function () {
    $(document).on("click", ".play-button svg", function (params) {
        params.preventDefault();
        const allPuasebtns = document.querySelectorAll(".pause-btn");
        for (let index = 0; index < allPuasebtns.length; index++) {
            const element = allPuasebtns[index];
            element.classList.remove("pause-btn");
            element.classList.add("play-button");
            element.parentElement.querySelector(".audio-file audio").pause();
            element.innerHTML = '<svg id="playIcon" width="64" height="64" viewBox="0 0 73 73" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="36.1522" cy="36.1522" r="24.8135" transform="rotate(45 36.1522 36.1522)" stroke="white" stroke-width="1.5" stroke-dasharray="19.66 7.87"/><path d="M46.3594 36.8017L47.4844 36.1522L46.3594 35.5027L31.6112 26.9878L30.4862 26.3383L30.4862 27.6373L30.4862 44.667L30.4862 45.9661L31.6112 45.3166L46.3594 36.8017Z" stroke="white" stroke-width="1.5"/></svg>';
        }
        
        const audioFile = this.parentElement.parentElement.querySelector(".audio-file audio");
        const playButton = this.parentElement.parentElement.querySelector(".play-button");
        playButton.classList.remove("play-button");
        playButton.classList.add("pause-btn");
        playButton.innerHTML = '<svg width="64" height="64" viewBox="0 0 73 73" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="36.1522" cy="36.1522" r="24.8135" transform="rotate(45 36.1522 36.1522)" stroke="white" stroke-width="1.5" stroke-dasharray="19.66 7.87"/><path d="M31 28V43.5" stroke="white" stroke-width="1.5"/><path d="M41 28V43.5" stroke="white" stroke-width="1.5"/></svg>';
        audioFile.play();
    })

    $(document).on("click", ".pause-btn svg", function (params) {
        params.preventDefault();
        const audioFile = this.parentElement.parentElement.querySelector(".audio-file audio");
        const pauseButton = this.parentElement;
        pauseButton.classList.remove("pause-btn");
        pauseButton.classList.add("play-button");
        pauseButton.innerHTML = '<svg id="playIcon" width="64" height="64" viewBox="0 0 73 73" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="36.1522" cy="36.1522" r="24.8135" transform="rotate(45 36.1522 36.1522)" stroke="white" stroke-width="1.5" stroke-dasharray="19.66 7.87"/><path d="M46.3594 36.8017L47.4844 36.1522L46.3594 35.5027L31.6112 26.9878L30.4862 26.3383L30.4862 27.6373L30.4862 44.667L30.4862 45.9661L31.6112 45.3166L46.3594 36.8017Z" stroke="white" stroke-width="1.5"/></svg>';
        audioFile.pause();
    })

    const audioFile = document.querySelector(".audio-file audio");
    const audioSlider = document.getElementById('rangePlay');
    const audioTimer = document.getElementById('playTime');

    audioFile.addEventListener("timeupdate", (event) => {
        var currentAudioTime = Math.round(audioFile.currentTime);
        const audioDuration = audioFile.duration;
        audioSlider.setAttribute("max", audioDuration);
        // console.log("The currentTime attribute has been updated. Again.", currentAudioTime);
        audioSlider.value = Math.floor(currentAudioTime);
        // console.log(audioSlider.value);
        audioSlider.style.backgroundSize = Math.round(audioSlider.value * 100 / audioSlider.max) + '% 100%';
        var minutes = 0;
        var seconds = '0';
        if(currentAudioTime > 59) {
            minutes = Math.floor(currentAudioTime/60)
        }
        if(Math.round(currentAudioTime - 60 * minutes) < 10) {
            seconds = '0' + Math.round(currentAudioTime - 60 * minutes)
        }
        else {
            seconds = Math.round(currentAudioTime - 60 * minutes)
        }

        audioTimer.innerHTML = minutes + ':' + seconds;
    });

    $('.slider-play').on('change', function() {
        let val = $(this).val();
        const audioFile = document.querySelector(".audio-file audio");
        audioFile.currentTime = val;
    });

    $('.slider-volume').on('change', function() {
        let val = $(this).val();
        const audioFile = document.querySelector(".audio-file audio");
        audioFile.volume = val / 100;
    });

    audioSlider.addEventListener("input", (event) => {
        audioSlider.style.backgroundSize = Math.round(audioSlider.value * 100 / audioSlider.max) + '% 100%'
    });

    const volumeSlider = document.getElementById('rangeVolume');
    volumeSlider.addEventListener("input", (event) => {
        volumeSlider.style.backgroundSize = Math.round(volumeSlider.value * 100 / volumeSlider.max) + '% 100%'
    });
    
     
  })(jQuery)
);