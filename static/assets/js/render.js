const REQUEST_URL = "http://127.0.0.1:8000";
const paths = {
    'directions': '/uzfi/direction/',
    'charter': '/uzfi/charter/',
    'documents': '/uzfi/document/',
    'councils':'/uzfi/councils/'
}


$(document).ready(function () {
    // render header
    $(".put-header").load('assets/components/header.html');
    // render footer
    $(".put-footer").load('assets/components/footer.html');
    let profileInfoSessions = ["profileInfoMissions", "profileInfoBio", "profileInfoCompletedMissions"];
    let profileInfoButtons = ["profileInfoMissionsBTN", "profileInfoBioBTN", "profileInfoCompletedMissionsBTN"];
    let hideprofileInfoSessions = () => profileInfoSessions.forEach(function (element) { $("#" + element).hide(); });
    hideprofileInfoSessions();
    $("#" + profileInfoSessions[0]).show();
    $("#" + profileInfoButtons[0]).addClass("sessions-active-button");
    profileInfoButtons.forEach(function (element) {

        $(`#${element}`).click(function (e) {
            hideprofileInfoSessions();
            $(`#${$(this).attr('data-for')}`).show();
            profileInfoButtons.forEach(function (el) {
                $(`#${el}`).removeClass("sessions-active-button");
            });
            $(this).addClass('sessions-active-button');

        });
    });






})



// Destinations
makeRequest(paths['directions'], function (data, statusText) {
    const destinations = $("#destinations .put-destinations");
    data.forEach(e => {
        destinations.append(`
        <div class="item">
            <div class="cours-bx">
                <div class="action-box">
                    <img src="assets/images/courses/pic1.jpg" alt="">
                    <a href="#" class="btn">Read More</a>
                </div>
                <div class="info-bx text-center">
                    <h5><a href="#">${e.name_en}</a></h5>
                    <span>${e.faculty.name}</span>
                </div>
                                
            </div>
        </div>
        `)
    })
}, function (e) { console.log(e) })


// Functions
function makeRequest(path, done, fail) {
    $.ajax({
        'method': 'get',
        'url': REQUEST_URL + path
    }).done(done).fail(fail)
}