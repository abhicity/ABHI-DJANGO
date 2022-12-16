function printTable() {

    var ps = Number(document.getElementById('txtNumber').value);
    var start = Number(document.getElementById('textNumber').value);
    var end = Number(document.getElementById('teextNumber').value);
    for (var i = start; i <= end; i++) {
        var pTag = document.getElementById('pPrint');
        pTag.innerHTML += "- " + (ps) + "*" + (i) + " = " + ps * i + "<br/>"
    }
}