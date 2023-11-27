

$(document).ready(function () {
  let profileInfoSessions = [
    "profileInfoMissions",
    "profileInfoBio",
    "profileInfoCompletedMissions",
  ];
  let profileInfoButtons = [
    "profileInfoMissionsBTN",
    "profileInfoBioBTN",
    "profileInfoCompletedMissionsBTN",
  ];
  let hideprofileInfoSessions = () =>
    profileInfoSessions.forEach(function (element) {
      $("#" + element).hide();
    });
  hideprofileInfoSessions();
  $("#" + profileInfoSessions[0]).show();
  $("#" + profileInfoButtons[0]).addClass("sessions-active-button");
  profileInfoButtons.forEach(function (element) {
    $(`#${element}`).click(function (e) {
      hideprofileInfoSessions();
      $(`#${$(this).attr("data-for")}`).show();
      profileInfoButtons.forEach(function (el) {
        $(`#${el}`).removeClass("sessions-active-button");
      });
      $(this).addClass("sessions-active-button");
    });
  });
});

