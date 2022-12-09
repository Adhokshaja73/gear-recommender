// write a function to submit answers for quiz
// it should sent an ajax post request to /quiz/submit with following parameters
// 1. quizId
// 2. selectedAnswer
// when response is received, if status is 1 in response, then add a div that says correct answer with green text
// else add a div that says wrong answer in red color and shows the correct answer from the response

function loadFirst(lesson, quizOfLessons) {
    lesson = lesson.replace(/'/g, '"');
    quizOfLessons = quizOfLessons.replace(/'/g, '"');

    lesson = JSON.parse(lesson)[0];
    console.log(lesson.video);
    const video = lesson.video;


    quizOfLessons = JSON.parse(quizOfLessons);
    currentQuiz = quizOfLessons[lesson.id];
    console.log(currentQuiz)

    const ab = document.getElementById('player');
    console.log(ab);
    ab.src = 'http://127.0.0.1:8000/' + video;
    ab.play()
    console.log(lesson);

    loadQuiz(currentQuiz);

}


function loadQuiz(currentQuiz) {
    document.getElementById('abc').innerHTML = ``;


    for (i = 0; i < currentQuiz.length; i++) {
        document.getElementById('abc').innerHTML += `
        
        <div class="col-xl-12 col-sm-12 col-12">
                            <div class="card shadow border-0">
                                <div class="card-body">
                                    <div class="row">
                                        <div class="col">
                                            <span class="h6 font-semibold text-muted text-sm d-block mb-2">
                                                <p id="abc">

                                                </p>

                                            </span>
                                            <span class="h3 font-bold mb-0">`
            + currentQuiz[i].question +
            `
                                                
                                            </span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                        <div class="row g-6 mb-3 mt-3">
                            <div class="col-xl-6 col-sm-6 col-6">
                                <div class="form-check">
                                    <div class="card shadow border-0" onclick = 'submitAnswer(`+ currentQuiz[i].id + `, 1)'>
                                        <div class="card-body">
                                            <div class="row">
                                                <div class="col">

                                                    <span
                                                        class="h6 font-semibold text-muted text-sm d-block mb-2">Option1</span>
                                                    <span class="h3 font-bold mb-0"><input class="form-check-input"
                                                            type="radio" name="flexRadioDefault" id="flexRadioDefault1">
                                                        <label class="form-check-label" for="flexRadioDefault1">
                                                            `
            + currentQuiz[i].option1 +
            `
                                                        </label></span>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-xl-6 col-sm-6 col-6">
                                <div class="form-check">

                                    <div class="card shadow border-0" onclick = 'submitAnswer(`+ currentQuiz[i].id + `, 2)'>
                                        <div class="card-body">
                                            <div class="row">
                                                <div class="col">
                                                    <span
                                                        class="h6 font-semibold text-muted text-sm d-block mb-2">Option
                                                        2</span>
                                                    <span class="h3 font-bold mb-0"><input class="form-check-input"
                                                            type="radio" name="flexRadioDefault" id="flexRadioDefault1">
                                                        <label class="form-check-label" for="flexRadioDefault1">`
            + currentQuiz[i].option2 + `
                                                        </label></span>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-xl-6 col-sm-6 col-6">
                                <div class="form-check">

                                    <div class="card shadow border-0" onclick = 'submitAnswer(`+ currentQuiz[i].id + `, 3)'>
                                        <div class="card-body">
                                            <div class="row">
                                                <div class="col">
                                                    <span
                                                        class="h6 font-semibold text-muted text-sm d-block mb-2">Option
                                                        3</span>
                                                    <span class="h3 font-bold mb-0">
                                                        <input class="form-check-input" type="radio"
                                                            name="flexRadioDefault" id="flexRadioDefault1">
                                                        <label class="form-check-label" for="flexRadioDefault1">
                                                            `
            + currentQuiz[i].option3 +
            `
                                                        </label>
                                                    </span>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-xl-6 col-sm-6 col-6">
                                <div class="form-check">

                                    <div class="card shadow border-0" onclick = 'submitAnswer(`+ currentQuiz[i].id + `, 4)'>
                                        <div class="card-body">
                                            <div class="row">
                                                <div class="col">
                                                    <span
                                                        class="h6 font-semibold text-muted text-sm d-block mb-2">Option
                                                        4</span>
                                                    <span class="h3 font-bold mb-0"><input class="form-check-input"
                                                            type="radio" name="flexRadioDefault" id="flexRadioDefault1">
                                                        <label class="form-check-label" for="flexRadioDefault1">
                                                            `
            + currentQuiz[i].option4 +
            `
                                                        </label></span>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>`;
        console.log("OH YEAH")
    }
}
function loadContent(lesson, quizOfLessons) {

    lesson = lesson.replace(/'/g, '"');
    quizOfLessons = quizOfLessons.replace(/'/g, '"');

    lesson = JSON.parse(lesson);
    console.log(lesson.video);
    const video = lesson.video;


    quizOfLessons = JSON.parse(quizOfLessons);
    currentQuiz = quizOfLessons[lesson.id];
    console.log(currentQuiz)

    const ab = document.getElementById('player');
    console.log(ab);
    ab.src = 'http://127.0.0.1:8000/' + video;
    ab.play()
    console.log(lesson);
    //document.getElementById("lesson-desc").innerHTML = lesson.description;
    // const question = document.getElementById("quiz-ques");
    // question.innerHTML = '';
    // question.innerHTML = lesson.quiz[0].question;
    // console.log(lesson.quiz[0].question);

    // var container = document.getElementById("quiz-ans");
    // //get length of lesson.quiz
    // var len = lesson.quiz.length;
    // console.log(len);
    // // 
    // var htmlElements = "";

    loadQuiz(currentQuiz);

}

function submitAnswer(quizId, selectedAnswer) {
    // write your code here
    $.ajax({   //ajax request
        url: '/quiz/submit',
        type: 'POST',
        data: {
            quizId: quizId,
            selectedAnswer: selectedAnswer,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function (response) {
            console.log(response);
            if (response.status == 1) {
                alert("Correct Answer");
            }
            else {
                alert("Wrong Answer");
            }

        }
    })
}


// write a function to update the lesson status for a user when the video element is played completely played
// send an ajax post request to /lesson/update-status with following parameters 
// 1. lessonId
// on sucess play the next video from the lessons 
function updateLessonStatus() {
    // write your code here
    $ajax({   //ajax request
        url: '/lesson/update-status',
        type: 'POST',
        data: {
            lessonId: lessonId
        },
        success: function (response) {
            // TODO play next video
        }
    })
}

