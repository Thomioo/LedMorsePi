var Send = function()
{
  // var orgSite = "http://192.168.2.241:8000/start";
  var s = document.getElementById("input").value;
  var site = "/say?s=" + s;
  fetch(site);
  console.log(site);
}