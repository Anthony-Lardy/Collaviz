{% extends 'base.html' %}
{% load static %}

{% block content %}
{% if request.method == "POST" %}
<button type="button" name="button" onclick="afficherChart({{donnees}})"></button>
{%endif %}
<div class="container">
  <div class="row justify-content-md-center text-center">
    <div id="insertionFichier">
      <h1>Collaviz</h1>
      <h3>Déposez le fichier à étudier : </h3>
      <form method="post" enctype="multipart/form-data">
        {% csrf_token %}
        <input type="file" name="fichier">
        <button type="submit">Déposer</button>
      </form>
      <div id="cont"></div>
    </div>
  </div>
  <!--previsualisation------------>
</div>
  <div class="container">
    <div class="row justify-content-md-center">
      <h2>Prévisualisation des données</h2>
    </div>
  </div>
  <div id="previsualisation">
    {% if request.method == "POST" %}
    <select class="browser-default custom-select" id="selectFile" onchange="afficherTableau()">
      <option selected disabled value=""></option>
      {% for o in file %}
      <option value="{{o}}">{{o}}</option>
      {% endfor %}
    </select>
    {%endif %}
    <div id="csv-display"> </div>
  </div>
  <!--Mapping------------>
  <div class="container">
    <div class="row justify-content-md-center">
      <h2>Mapping</h2>
    </div>
  </div>            {% csrf_token %}

  <div id="mapping" class="row justify-content-md-center">
    <div class="col-12">
      {% if request.method == "POST" %}
      <select class="browser-default custom-select" id="mappingFichier" onchange="getColonnes()">
        <option name="null" selected disabled value="test"></option>
        {% for o in file %}
        <option  value="{{o}}">{{o}}</option>
        {% endfor %}
      </select>
      {%endif %}
    </div>
    <div id="user" class="col-4">
      <h4>Utilisateur : </h4>
      <select id="utilisateurCol" class="browser-default custom-select"> </select>
    </div>
    <div id="date" class="col-4">
      <h4>Date : </h4>
      <select id="dateCol" class="browser-default custom-select"> </select>
    </div>
    <div id="heure" class="col-4">
      <h4>Heure : </h4>
      <select id="heureCol" class="browser-default custom-select"> </select>
    </div><br><br><br><br><br>
    <div id="action" class="col-4">
      <h4>Action : </h4>
      <select id="actionCol" class="browser-default custom-select"></select>
    </div><br><br><br><br>
    <div class="row col-12">
      <div class="col-6">
        <label>"Répondre à un message : "</label>
        <input id="repondreMessage" class="w3-input" type="text">
      </div>
      <div class="col-6">
        <label>"Créer un nouveau message :"</label>
        <input id="creerMessage" class="w3-input" type="text">
      </div>
    </div>
    <div id="attribut" class="col-4">
      <h4>Attribut : </h4>
      <select id="attributCol" class="browser-default custom-select"></select>
    </div><br><br><br><br>
    <div class="row col-12">
      <div class="col-4">
        <label>idForum : </label>
        <input id="idForum" class="w3-input" type="text">
      </div>
      <div class="col-4">
        <label>idMessage :</label>
        <input id="idMessage" class="w3-input" type="text">
      </div>
      <div class="col-4">
        <label>idParent :</label>
        <input id="idParent" class="w3-input" type="text">
      </div>
    </div>
    <div class="col-3">
    <button type="button" id="validerMapping" class="btn btn-success">Valider le mapping</button>
    </div>
  </div>
      <br><br><br><br><br>
  <div class="row" id="test">
    <div class="col-1">
      <div id="toolbar" class="icon-bar">
        <a id="graphCamembert" ><i class="fas fa-chart-pie"></i></a>
        <a id="graph" ><i class="fas fa-chart-area"></i></a>
        <a id="graphBarre"><i class="fas fa-chart-bar"></i></a>
      </div>
      </div>
      <div class="gridly col-11">
      </div>


      </div>
  <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>



<script type="text/javascript">

  var i = 0;

  $( "#graph" ).click(function( event ) {
    ajouterCadre(event);
    ajouterChampsGraph(i);
    div = "container"+i+""
    ajouterGraph(div);
    i = i+1;
  });




  function ajouterChampsGraph(i){
    var html="<p>nbAction(s): <select id='selectNbAction' class='selectpicker' data-live-search='true'></p><option>Connexion</option>";
        html +="<option>Répondre à un message</option><option>Poster un message</option><option>Accéder à la file</option></select>";
        html +="<p>Utilisateur(s): <select id='selectUtilisateurs' class='selectpicker' multiple data-live-search='true'></p><option>Mmay</option>";
        html +="<option>Ketchup</option><option>Relish</option></select><p>Date de début: <input id='dateDeb' type='date' id='datepicker'></p>";
        html+= "<p>Date de fin: <input id='dateFin' type='date' id='datepicker'><button type='button' id='envoyerParamsGraph' class='btn btn-success'>Valider les paramètres</button>";
        html+="<div id='container"+i+"'></div>";
          $('.brick').last().append(html);

  }

  function ajouterGraph(container){
    Highcharts.chart(container, {

    title: {
        text: 'Solar Employment Growth by Sector, 2010-2016'
    },

    subtitle: {
        text: 'Source: thesolarfoundation.com'
    },

    yAxis: {
        title: {
            text: 'Number of Employees'
        }
    },

    xAxis: {
        accessibility: {
            rangeDescription: 'Range: 2010 to 2017'
        }
    },

    legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'middle'
    },

    plotOptions: {
        series: {
            label: {
                connectorAllowed: false
            },
            pointStart: 2010
        }
    },

    series: [{
        name: 'Installation',
        data: [43934, 52503, 57177, 69658, 97031, 119931, 137133, 154175]
    }, {
        name: 'Manufacturing',
        data: [24916, 24064, 29742, 29851, 32490, 30282, 38121, 40434]
    }, {
        name: 'Sales & Distribution',
        data: [11744, 17722, 16005, 19771, 20185, 24377, 32147, 39387]
    }, {
        name: 'Project Development',
        data: [null, null, 7988, 12169, 15112, 22452, 34400, 34227]
    }, {
        name: 'Other',
        data: [12908, 5948, 8105, 11248, 8989, 11816, 18274, 18111]
    }],

    responsive: {
        rules: [{
            condition: {
                maxWidth: 500
            },
            chartOptions: {
                legend: {
                    layout: 'horizontal',
                    align: 'center',
                    verticalAlign: 'bottom'
                }
            }
        }]
    }

    });
  }


  $( ".delete" ).click(function( event ) {

    $(this).closest('.brick').remove();
  });

    $('.gridly').gridly({
      base: 100, // px
      gutter: 20, // px
      columns: 12
    });
  $(function() {

        $("#validerMapping").click( function()
             {  $("#idMessage").val();
               $.ajax({
               type: "POST",
               url: "/mappingDonnees",
               data: {fichier: $("#mappingFichier").find('option:selected').text(), utilisateur: $("#utilisateurCol").find('option:selected').text(), heure: $("#heureCol").find('option:selected').text(),
               date: $("#dateCol").find('option:selected').text(), titre: $("#actionCol").find('option:selected').text(), attribut: $("#attributCol").find('option:selected').text(),
                repondre: $("#repondreMessage").val(), poster: $("#creerMessage").val(), forum: $("#idForum").val(),
                message: $("#idMessage").val(), parent: $("#idParent").val()},
               success: function (data, text) {
                 alert("ca marche")

               },
               error: function (request, status, error) {
                   alert(request.responseText);
               }
              }
              );
             }
        );
  });








  function afficherTableau() {
    $.ajax({

      url: "../media/tmp/" + $("#selectFile").val(),
      dataType: "text",
      success: function(data) {
        data = $.csv.toArrays(data);
        generateHtmlTable(data);
      }

    });

  }

  function getColonnes() {
    //utilisateur, date, heure, titre, attribut
    $.ajax({

      url: "../media/tmp/" + $("#mappingFichier").val(),
      dataType: "text",
      success: function(data) {
        selectNom = ["utilisateur", "date", "heure", "action", "attribut"];
        var titre = data.trim().split('\n')[0].split(',');
        for (var i = 0; i < selectNom.length; i++) {
          $('#' + selectNom[i] + 'Col').html("");
          $('#' + selectNom[i] + 'Col').append($('<option selected>', {
            value: "",
            text: ""
          }));
          for (var j = 0; j < titre.length; j++) {
            $('#' + selectNom[i] + 'Col').append($('<option>', {
              value: j,
              text: titre[j]
            }));
          }

        }
      }

    });

  }

  function generateHtmlTable(data) {

    var html = '<table id="table" class="table table-condensed table-hover table-striped">';

    if (typeof(data[0]) === 'undefined') {
      return null;
    } else {
      $.each(data, function(index, row) {
        //bind header
        if (index == 0) {
          html += '<thead>';
          html += '<tr>';
          $.each(row, function(index, colData) {
            html += '<th>';
            html += colData;
            html += '</th>';
          });
          html += '</tr>';
          html += '</thead>';
          html += '<tbody>';
        } else {
          html += '<tr>';
          $.each(row, function(index, colData) {
            html += '<td>';
            html += colData;
            html += '</td>';
          });
          html += '</tr>';
        }
      });
      html += '</tbody>';
      html += '</table>';
      $('#csv-display').html(html);
    }
    $('#table').DataTable();

  }
</script>


{% endblock %}
