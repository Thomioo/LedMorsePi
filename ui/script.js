var On = function()
{
  // var orgSite = "http://192.168.2.241:8000/start";
  var site = document.getElementById("address").value.toString() + "/on";
  fetch(site, { mode: 'no-cors' });
}
var Off = function()
{
  var site = document.getElementById("address").value.toString() + "/off";
  // fetch(site, { mode: 'no-cors' });
  fetch(site);

}