$(".plant").on("click", function (event) { // chaque espèce dans le panel de recherche
    var value = parseInt($(this).data("value"));
    add_node(value);
    restart();
    select_node(value);
    event.stopPropagation();
});
// pour la fenêtre d'initialisation
$(".reset-btn").on("click", function () {
    restart_with_list($(this).data("plants").split("|"));
    $('#save-btn').addClass("hidden");
});
// bouton wiki du panel en bas à gauche
$("#wiki-btn").on("click", function (event) {
    event.stopPropagation();
});

$("#ncbi-btn").on("click", function (event) {
    event.stopPropagation();
});

var jetsearch = Jets({
    searchTag: "#jets-MonPotager-search",
    contentTag: "#jets-MonPotager-content"
});

function restart_with_list(str_list) {
    var int_list = $.map(graph.nodes.filter(function (val) {
            return str_list.includes(val.name)
        }),
        function (node) {
            return node.value
        });
    remove_nodes();
    for (var i = 0; i < int_list.length; i++) {
        add_node(int_list[i])
    }
    restart();
}
// span des éléments du panel en haut à gauche (plantes,nuisible,axiliaires) cachés ou pas
$(".potager-item").on("click", function (event) {
    var value = parseInt($(this).data("value"));
    select_node(value);
    event.stopPropagation();
});
// corbeille du panel en bas à gauche
$("#remove-selected").on("click", function (event) {
    remove_node(parseInt($(this).data("value")));
    restart();
    event.stopPropagation();
}); // filtre de recherche (panel à droite)
$("#filter").on("click", function (event) {
    $(this).addClass("hidden");
    $(".plant").removeClass("filtered");
    event.stopPropagation();
});

function filter_plantes(index, direction, interaction) {
    var cur_node = graph.nodes[index];
    var $plants = $(".plant");
    $plants.removeClass("filtered");
    $("#jets-MonPotager-search").val('');
    jetsearch.search();
    var $filter = $("#filter");
    if (["pos", "atr"].includes(interaction)) {
        $filter.removeClass('btn-danger').addClass('btn-success')
    } else {
        $filter.addClass('btn-danger').removeClass('btn-success')
    }
    var opposite_direction = (direction === "forward") ? "backward" : "forward";
    $("#filter-name").html(filter_name_dico[opposite_direction][interaction] + " " + cur_node.name.toLowerCase() + " ");
    $filter.removeClass("hidden");
    $plants.each(function () {
        var $this = $(this);
        var thisIndex = parseInt($this.data("value"));
        var connected = graph[direction][index].filter(function (l) {
            return ((typeof l.target !== "undefined") ? l.target : l.source) === thisIndex && l.value === interaction
        });
        if (connected.length === 0) {
            $this.addClass("filtered")
        }
    });
}
//panel en bas à gauche : section favorise etc
$(".btn-filter").on("click", function (event) {
    var index = $(this).data("value");
    var direction = $(this).data("direction");
    var interaction = $(this).data("interaction");
    filter_plantes(index, direction, interaction);
});

function direction_interaction(direction, interaction, index) {
    var list_ids = $.map(graph[direction][index].filter(function (l) {
        return l.value === interaction
    }), function (val) {
        return (typeof val.source !== "undefined") ? val.source : val.target
    });
    var graph_list_ids = list_ids.filter(function (val) {
        return index_nodes.includes(val)
    });
    if (graph_list_ids.length > 0) {
        $(".text", "#node-" + direction + "-" + interaction).text($.map(graph_list_ids, function (val) {
            return " " + graph.nodes[val].name
        }));
    } else {
        $(".text", "#node-" + direction + "-" + interaction).html("&#8709;")
    }

    var $button = $(".btn-filter", "#node-" + direction + "-" + interaction);
    $button.removeClass("hidden");
    var other_interactions = list_ids.filter(function (x) {
        return !graph_list_ids.includes(x)
    }).length;

    if (other_interactions > 0) {
        $button.data('direction', direction);
        $button.data('interaction', interaction);
        $button.data('value', index);
        $button.text(". +" + String(other_interactions) + " dans l'inventaire");
    } else {
        $button.addClass("hidden");
    }
    if (graph_list_ids.length === 0 && other_interactions === 0) {
        $("#node-" + direction + "-" + interaction, "#info").addClass("hidden")
    } else {
        $("#node-" + direction + "-" + interaction, "#info").removeClass("hidden")
    }
}

function select_node(index) {
    is_selected = true;
    no_transparence();
    transparent(index);
    var cur_node = graph.nodes[index];
    var $removeSelected = $("#remove-selected");
    if (cat_animals.includes(cur_node.group)) {
        $removeSelected.addClass("hidden");
    } else {
        $removeSelected.removeClass("hidden");
        $removeSelected.data("value", index);
    }
    var $helpers_links = $("#helpers-links");
    $helpers_links.addClass("hidden");
    $(".helpers-item", "#helpers-container").remove();
    ["forward", "backward"].forEach(function (direction) {
        interactions.forEach(function (interaction) {
            direction_interaction(direction, interaction, index)
        });
    });

    if (cat_pests.includes(graph.nodes[index].group)) {
        var plus = $.map(graph.backward[index].filter(function (l) {
            return l.value === "rep" && cat_helpers.includes(l.group);
        }), function (val) {
            return val.source;
        });
        if (plus.length > 0) {
            $helpers_links.removeClass("hidden");
            var $helpers_container = $("#helpers-container");
            plus.forEach(function (helper) {
                var d = document.createElement('span');
                $(d).addClass('helpers-item links')
                    .html(graph.nodes[helper].name + "; ")
                    .data("value", helper)
                    .appendTo($helpers_container)
            });
            $(".helpers-item", "#helpers-container").on("click", function (event) {
                var index = parseInt($(this).data("value"));
                filter_plantes(index, "backward", "atr");
            });
        }
        $("#glyph-backward-atr", "#info").removeClass("glyphicon-ok-circle green").addClass("glyphicon-remove-circle red");
        $("#glyph-backward-rep", "#info").removeClass("glyphicon-remove-circle red").addClass("glyphicon-ok-circle green");
    } else {
        $("#glyph-backward-rep", "#info").removeClass("glyphicon-ok-circle green").addClass("glyphicon-remove-circle red");
        $("#glyph-backward-atr", "#info").removeClass("glyphicon-remove-circle red").addClass("glyphicon-ok-circle green");
    }

    var $plants = $(".plant");
    $plants.removeClass("filtered");
    $("#info-name").text(cur_node.name + " (" + groups[cur_node.group].toLowerCase() + ")");
    $("#info").removeClass("hidden");
    var $wiki_btn = $("#wiki-btn");
    if (cur_node.wiki.length === 0) {
        $wiki_btn.addClass("hidden")
    } else {
        $wiki_btn.removeClass("hidden");
        $wiki_btn.attr("href", cur_node.wiki);
    }
    var $ncbi_btn = $("#ncbi-btn");
    if (cur_node.ncbi.length === 0) {
        $ncbi_btn.addClass("hidden")
    } else {
        $ncbi_btn.removeClass("hidden");
        $ncbi_btn.attr("href", cur_node.ncbi);
    }
}

var svg = d3.select("#graph"),
    width = +$(window).width(),
    height = +$(window).height();

var nodes = [], index_nodes = [], links = [];
var is_selected = false;
svg.append("defs").selectAll("marker")
    .data(interactions)
    .enter().append("marker")
    .attr("id", function (d) {
        return d;
    })
    .attr("viewBox", "0 -5 10 10")
    .attr("refX", 15)
    .attr("refY", -1.5)
    .attr("markerWidth", 6)
    .attr("markerHeight", 6)
    .attr("orient", "auto")
    .append("path")
    .attr("d", "M0,-5L10,0L0,5");


var simulation = d3.forceSimulation(nodes)
    .force("link", d3.forceLink(links).distance(200).strength(0.2))
    .force("charge", d3.forceManyBody().strength(-600))
    .force("x", d3.forceX())
    .force("y", d3.forceY())
    .on("tick", tick);

var g = svg.append("g"),
    link = g.append("g").attr("class", "links").selectAll(".link"),
    node = g.append("g").attr("class", "nodes").selectAll(".node");

svg.attr("viewBox", (-width / 2) + " " + (-height / 2) + " " + (width) + " " + (height))
    .attr("width", width)
    .attr("height", height)
    .style("pointer-events", "visible");

//Function to the css rule
function checkSize() {
    if ($("#on-screen-test").css("float") === "none") {
        console.log("On Screen");
        svg.call(d3.zoom(1)
            .scaleExtent([1 / 4, 4])
            .on("zoom", zoomed));
    } else {
        console.log("On mobile");
        svg.on(".zoom", null);
    }
}

function zoomed() {
    g.attr("transform", d3.event.transform.scale(1));
}

function remove_nodes() {
    $(".plant", "#jets-MonPotager-content").removeClass("hidden");
    $(".potager-item", "#upper-left").addClass("hidden");
    $(".potager-item", "#plantCalendar").addClass("hidden");/*Permet de supprimer du calendrier la ligne de la plante*/
    $(".padding-div", "#upper-left").addClass("hidden");
    index_nodes = [];
    nodes = [];
    links = [];
}

function show_item_div(div_id, nbr_items) {
    if (nbr_items === 0) {
        $('#' + div_id).addClass("hidden");
    } else {
        $('#' + div_id).removeClass("hidden");
        var span_text = $('#' + div_id + "-count");
        if (nbr_items > 1) {
            span_text.html(nbr_items + " " + span_text.data("plural"));
        } else {
            span_text.html(nbr_items + " " + span_text.data("singular"));
        }
    }
}

function show_items() {
    var relevant_links = links;
    nodes.forEach(function (tmp_node) {
        if (cat_pests.includes(tmp_node.group)) {
            if (links.filter(function (l) {
                return (l.target.value === tmp_node.value && ["rep"].includes(l.value));
            }).length > 0) {
                relevant_links = relevant_links.filter(function (l) {
                    return !(l.source.value === tmp_node.value || l.target.value === tmp_node.value);
                });
                $(".potager-item-" + String(tmp_node.value), "#repelled-pests").removeClass("hidden");
                $(".potager-item-" + String(tmp_node.value), "#pests").addClass("hidden");
            } else {
                $(".potager-item-" + String(tmp_node.value), "#repelled-pests").addClass("hidden");
                $(".potager-item-" + String(tmp_node.value), "#pests").removeClass("hidden");
            }
        }
    });
    ["pos", "neg"].forEach(function (inter) {
        var nbr_links = relevant_links.filter(function (l) {
            return inter === l.value;
        }).length;
        show_item_div("interaction-" + inter, nbr_links);
    });
    ["plants", "repelled-pests", "pests", "helpers"].forEach(function (div_id) {
        var $items = $(".potager-item", '#' + div_id);
        var displayed_items = $items.length - $items.filter(".hidden").length;
        show_item_div(div_id, displayed_items);
    });
}

function remove_node(cur_index) {
    var cur_node = graph.nodes[cur_index];
    if (cat_plants.includes(cur_node.group)) {
        $("#plant-" + String(cur_index), "#jets-MonPotager-content").removeClass("hidden");
    }
    $(".potager-item-" + String(cur_index), "#upper-left").addClass("hidden");
    $(".potager-item-" + String(cur_index), "#plantCalendar").addClass("hidden");/*Permet de supprimer du calendrier la ligne de la plante*/

    var i = index_nodes.indexOf(cur_index);
    index_nodes.splice(i, 1);
    nodes.splice(i, 1);

    links = links.filter(function (l) {
        return l.source.value !== cur_index && l.target.value !== cur_index;
    });

    nodes.forEach(function (tmp_node) {
        if (cat_animals.includes(tmp_node.group)) {
            if (links.filter(function (l) {
                var atr_rep = (l.target.value === tmp_node.value) && ["atr", "rep"].includes(l.value);
                var neg_pos = (l.source.value === tmp_node.value) && ["neg", "pos"].includes(l.value);
                return neg_pos || atr_rep;
            }).length === 0) {
                remove_node(tmp_node.value)
            }
        }
    });
}

function add_node(cur_index, add_links) {
    add_links = typeof add_links !== 'undefined' ? add_links : true;

    index_nodes.push(cur_index);
    var cur_node = graph.nodes[cur_index];
    nodes.push(cur_node);

    if (cat_plants.includes(cur_node.group)) {
        $("#plant-" + String(cur_index), "#jets-MonPotager-content").addClass("hidden");
    }
    $(".potager-item-" + String(cur_node.value), "#upper-left").removeClass("hidden");
    $(".potager-item-" + String(cur_node.value), "#plantCalendar").removeClass("hidden");/*Permet d'ajouter au calendrier la ligne de la plante*/

    if (add_links) {
        for (var f = 0; f < graph.forward[cur_index].length; f++) {
            var f_link = graph.forward[cur_index][f];
            if (index_nodes.includes(f_link.target)) {
                links.push({"source": cur_node, "target": graph.nodes[f_link.target], "value": f_link.value});
            } else if (cat_animals.includes(f_link.group) && ["atr", "rep"].includes(f_link.value)) {
                add_node(f_link.target);
            }
        }
        for (var b = 0; b < graph.backward[cur_index].length; b++) {
            var b_link = graph.backward[cur_index][b];
            if (index_nodes.includes(b_link.source)) {
                links.push({"source": graph.nodes[b_link.source], "target": cur_node, "value": b_link.value});
            } else if (cat_animals.includes(b_link.group) && ["neg", "pos"].includes(b_link.value)) {
                add_node(b_link.source);
            }
        }
    }
}

function restart() {

    // Apply the general update pattern to the nodes.
    node = node.data(nodes, function (d) {
        return d.value;
    });
    node.exit().remove();
    node = node.enter().append("g").attr("class", "node ").each(function () {
        d3.select(this).insert("circle")
            .attr("fill", function (d) {
                return color[d.group]
            })
            .attr("r", 10)
            .attr("value", function (d) {
                return d.value
            })
            .attr("data-toggle", "tooltip")
            .attr("title", function (d) {
                return groups[graph.nodes[parseInt(d.value)].group]
            });
        d3.select(this).insert("text")
            .attr("x", 11)
            .attr("y", -4)
            .text(function (d) {
                return d.name;
            })
    }).merge(node);

    // Apply the general update pattern to the links.
    link = link.data(links, function (d) {
        return d.source.value + "-" + d.target.value;
    });
    link.exit().remove();
    link = link.enter().append("path")
        .attr("class", function (d) {
            return "link " + d.value;
        })
        .attr("marker-end", function (d) {
            return "url(#" + d.value + ")";
        })
        .merge(link);


    $(".plant").each(function () {
        var $this = $(this);
        var value = $this.data("value");
        $(".plus", $this).text(String(
            graph.forward[value].filter(function (l) {
                return index_nodes.includes(l.target) && l.value === "pos"
            }).length +
            graph.backward[value].filter(function (l) {
                return index_nodes.includes(l.source) && l.value === "pos"
            }).length
        ));
        $(".minus", $this).text(String(
            graph.forward[value].filter(function (l) {
                return index_nodes.includes(l.target) && l.value === "neg"
            }).length +
            graph.backward[value].filter(function (l) {
                return index_nodes.includes(l.source) && l.value === "neg"
            }).length
        ))
    });
    $('[data-toggle="tooltip"]').tooltip({container: "body"});
    $("circle").on({ //pour les nodes du graphe
        mouseenter: function () {
            if (!is_selected) {
                no_transparence();
                transparent($(this).attr("value"))
            }
        },
        mouseleave: function () {
            if (!is_selected) {
                no_transparence();
                transparence_pest();
            }
        },
        click: function (event) {
            document.getElementById("myInput3").value = $(this).parent().children()[1].innerHTML;
            select_node($(this).attr("value"));
            event.stopPropagation();
        }
    });
    $("#filter").click();
    $("#info").addClass("hidden");
    $('#save-btn').removeClass("hidden");
    is_selected = false;
    no_transparence();
    transparence_pest();
    show_items();

    // Update and restart the simulation.
    simulation.nodes(nodes);
    simulation.force("link").links(links);
    simulation.alpha(1).restart();
}

function transparent(index) {
    var cur_node = graph.nodes[index];
    link.filter(function (l) {
        return l.source.value !== cur_node.value && l.target.value !== cur_node.value;
    }).transition().style("opacity", "0.12");
    node.filter(function (d) {
        return d !== cur_node & graph.forward[index].filter(function (l) {
            return l.target === d.value
        }).length === 0 & graph.backward[index].filter(function (l) {
            return l.source === d.value
        }).length === 0
    }).transition().style("opacity", "0.12");
}

function no_transparence() {
    link.transition().style("opacity", "1");
    node.transition().style("opacity", "1");
}

function transparence_pest() {
    nodes.forEach(function (tmp_node) {
        if (cat_pests.includes(tmp_node.group)) {
            var filtered_links = links.filter(function (l) {
                return (l.target.value === tmp_node.value && ["rep"].includes(l.value));
            });
            if (filtered_links.length > 0) {
                link.filter(function (l) {
                    return l.source.value === tmp_node.value || l.target.value === tmp_node.value;
                }).transition().style("opacity", "0.12");
                node.filter(function (d) {
                    return d === tmp_node;
                }).transition().style("opacity", "0.12");
            }
        }
    });
}

$(document).on('click', function (evt) {
    if (is_selected) {
        $("#info").addClass("hidden");
        is_selected = false;
        no_transparence();
        transparence_pest();
    }
});

function tick() {
    node.attr("transform", function (d) {
        return "translate(" + d.x + "," + d.y + ")";
    });

    link.attr("d", function (d) {
        var dx = d.target.x - d.source.x,
            dy = d.target.y - d.source.y,
            dr = Math.sqrt(dx * dx + dy * dy);
        return "M" + d.source.x + "," + d.source.y + "A" + dr + "," + dr + " 0 0,1 " + d.target.x + "," + d.target.y;
    })
}
// pour les lettres de la recherche (panel à droite)
$('.btn-letter').on("click", function (event) {
    var letter = $(this).data("letter");
    var not_hidden = $('.btn-plant').filter(function (i) {
        return !$(this).hasClass("hidden");
    });
    var sup_letter = not_hidden.filter(function (i) {
        return $(this).data("letter") >= letter;
    });
    if (not_hidden.length >= 1) {
        if (sup_letter.length >= 1) {
            $('#jets-MonPotager-content').scrollTo(sup_letter[0], 500);
        } else {
            $('#jets-MonPotager-content').scrollTo(not_hidden[not_hidden.length - 1], 500);
        }
    }
    event.stopPropagation();
});


// fonction cachant le bouton de sauvegarde
$('#save-btn').on("click", function (event) {
    var saves = Cookies.getJSON("saves");
    if (typeof saves === "undefined") {
        saves = [];
    }
    var plante_nodes = $.map(nodes.filter(function (n) {
        return cat_plants.includes(n.group);
    }), function (node) {
        return node.name;
    });
    var save = {};
    var currentdate = new Date();
    save.date = currentdate.getDate() + "/"
        + (currentdate.getMonth() + 1) + "/"
        + currentdate.getFullYear() + " @ "
        + currentdate.getHours() + ":"
        + currentdate.getMinutes() + ":"
        + currentdate.getSeconds();
    save.nbr_nodes = plante_nodes.length;
    save.nodes = plante_nodes;
    saves.push(save);
    Cookies.set("saves", saves, {expires: 3650});
    $(this).addClass("hidden");
    var d = document.createElement('div');
    $(d).addClass('alert alert-success alert-dismissible')
        .html("<a href='#' class='close' data-dismiss='alert' aria-label='close'>&times;</a><strong>Potager sauvergardé.</strong>")
        .appendTo("#alert-save");
    event.stopPropagation();
});

function display_saves() {
    var saves = Cookies.getJSON("saves");
    if (typeof saves === "undefined") {
        saves = [];
    }
    if (saves.length >= 1) {
        $('#my-saves').removeClass("hidden")
    } else {
        $('#my-saves').addClass("hidden");
    }
    var $my_saves = $('#my-save-list');
    $my_saves.html("");
    saves.forEach(function (save) {
        // Add inner html
        var d = document.createElement('div');
        $(d).addClass('save-reset')
            .html("<span class=\"glyphicon glyphicon-open\"></span> " + save.date + " (" + save.nbr_nodes + " plantes)")
            .data("plants", save.nodes.join('|'))
            .appendTo($my_saves)
    });
    // for all buttons, activate behavior
    $('.save-reset').on("click", function (event) {
        restart_with_list($(this).data("plants").split("|"));
        $('#save-btn').addClass("hidden");
        $('#reset').modal('hide');
    });
}

$('#saves-remove').on("click", function (event) {
    Cookies.set("saves", [], {expires: 3650});
    display_saves();
    event.stopPropagation();
});

$('#reset').on('show.bs.modal', function () {
    display_saves()
});


$(document).ready(function () {
    // run test on initial page load
    checkSize();

    // run test on resize of the window
    $(window).resize(checkSize);

    show_items();
    $('#save-btn').addClass("hidden");
    $('#reset').modal('show');
    var $collapse = $('.collapse');
    $collapse.on('show.bs.collapse', function () {
        $(this).parent(".panel").find(".text-left").html("Masquer la légende");
        $(this).parent("div").parent("div").find(".glyphicon-chevron-up").removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down");

    });
    $collapse.on('hide.bs.collapse', function () {
        $(this).parent("div").parent("div").find(".text-left").html("Afficher la légende");
        $(this).parent(".panel").find(".glyphicon-chevron-down").removeClass("glyphicon-chevron-down").addClass("glyphicon-chevron-up");

    });
});








// code pour l'autocomplétion dans les formulaires



function autocomplete(inp, arr) {
  /*the autocomplete function takes two arguments,
  the text field element and an array of possible autocompleted values:*/
  var currentFocus;
  /*execute a function when someone writes in the text field:*/
  inp.addEventListener("input", function(e) {
      var a, b, i, val = this.value;
      /*close any already open lists of autocompleted values*/
      closeAllLists();
      if (!val) { return false;}
      currentFocus = -1;
      /*create a DIV element that will contain the items (values):*/
      a = document.createElement("DIV");
      a.setAttribute("id", this.id + "autocomplete-list");
      a.setAttribute("class", "autocomplete-items");
      /*append the DIV element as a child of the autocomplete container:*/
      this.parentNode.appendChild(a);
      /*for each item in the array...*/
      for (i = 0; i < arr.length; i++) {
        /*check if the item starts with the same letters as the text field value:*/
        if (arr[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
          /*create a DIV element for each matching element:*/
          b = document.createElement("DIV");
          /*make the matching letters bold:*/
          b.innerHTML = "<strong>" + arr[i].substr(0, val.length) + "</strong>";
          b.innerHTML += arr[i].substr(val.length);
          /*insert a input field that will hold the current array item's value:*/
          b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
          /*execute a function when someone clicks on the item value (DIV element):*/
          b.addEventListener("click", function(e) {
              /*insert the value for the autocomplete text field:*/
              inp.value = this.getElementsByTagName("input")[0].value;
              /*close the list of autocompleted values,
              (or any other open lists of autocompleted values:*/
              closeAllLists();
          });
          a.appendChild(b);
        }
      }
  });
  /*execute a function presses a key on the keyboard:*/
  inp.addEventListener("keydown", function(e) {
      var x = document.getElementById(this.id + "autocomplete-list");
      if (x) x = x.getElementsByTagName("div");
      if (e.keyCode == 40) {
        /*If the arrow DOWN key is pressed,
        increase the currentFocus variable:*/
        currentFocus++;
        /*and and make the current item more visible:*/
        addActive(x);
      } else if (e.keyCode == 38) { //up
        /*If the arrow UP key is pressed,
        decrease the currentFocus variable:*/
        currentFocus--;
        /*and and make the current item more visible:*/
        addActive(x);
      } else if (e.keyCode == 13) {
        /*If the ENTER key is pressed, prevent the form from being submitted,*/
        e.preventDefault();
        if (currentFocus > -1) {
          /*and simulate a click on the "active" item:*/
          if (x) x[currentFocus].click();
        }
      }
  });
  function addActive(x) {
    /*a function to classify an item as "active":*/
    if (!x) return false;
    /*start by removing the "active" class on all items:*/
    removeActive(x);
    if (currentFocus >= x.length) currentFocus = 0;
    if (currentFocus < 0) currentFocus = (x.length - 1);
    /*add class "autocomplete-active":*/
    x[currentFocus].classList.add("autocomplete-active");
  }
  function removeActive(x) {
    /*a function to remove the "active" class from all autocomplete items:*/
    for (var i = 0; i < x.length; i++) {
      x[i].classList.remove("autocomplete-active");
    }
  }
  function closeAllLists(elmnt) {
    /*close all autocomplete lists in the document,
    except the one passed as an argument:*/
    var x = document.getElementsByClassName("autocomplete-items");
    for (var i = 0; i < x.length; i++) {
      if (elmnt != x[i] && elmnt != inp) {
        x[i].parentNode.removeChild(x[i]);
      }
    }
  }
  /*execute a function when someone clicks in the document:*/
  document.addEventListener("click", function (e) {
      closeAllLists(e.target);
  });
}

// fonction du formulaire des interactions pour intervertir espèces

function swap() {
    var temp = $("#myInput3").val();
    $("#myInput3").val($("#myInput4").val());
    $("#myInput4").val(temp);
}


// fonctions pour la prise en compte des formulaires


function submit_specie() {
    var nameesp = document.getElementById("specieName");
    var scientiesp = document.getElementById("myInput2");
    var catesp = document.getElementById("inputcat");

    var entryint = {
        namaesp : nameesp.value,
        scientiesp: scientiesp.value,
        catesp: catesp.value
    };

    fetch(`${window.origin}/species/new-entry`, {
      method: "POST",
      credentials: "include",
      body: JSON.stringify(entryint),
      cache: "no-cache",
      headers: new Headers({
        "content-type": "application/json"
      })
    })
      .then(function (response) {
        if (response.status !== 200) {
          console.log(`Looks like there was a problem. Status code: ${response.status}`);
          alert(`Une ERREUR a été rencontrée lors de l'ajout : Status code: ${response.status}`);
          return;
        }
        response.json().then(function (data) {
          console.log(data);
          alert("L'espèce a été ajoutée avec succès !");
          location.reload(true);
        });
      })
      .catch(function (error) {
        console.log("Fetch error: " + error);
        alert("Une ERREUR a été rencontrée : "  + error);
      });
}

function submit_interaction() {
    var espSource = document.getElementById("myInput3");
    var espCible = document.getElementById("myInput4");
    var espInteraction = document.getElementById("inputIntType");

    var entryint = {
        espSource : espSource.value,
        espCible: espCible.value,
        espInteraction: espInteraction.value
    };

    fetch(`${window.origin}/association/new-entry`, {
      method: "POST",
      credentials: "include",
      body: JSON.stringify(entryint),
      cache: "no-cache",
      headers: new Headers({
        "content-type": "application/json"
      })
    })
      .then(function (response) {
        if (response.status !== 200) {
          console.log(`Looks like there was a problem. Status code: ${response.status}`);
          alert(`Une ERREUR a été rencontrée lors de l'ajout : Status code: ${response.status}`);
          return;
        }
        response.json().then(function (data) {
          console.log(data);
          alert("L'intéraction a été ajoutée avec succès !");
          location.reload(true);
        });
      })
      .catch(function (error) {
        console.log("Fetch error: " + error);
        alert("Une ERREUR a été rencontrée : "  + error);
      });
}



/*An array containing all the species*/

var availableTags = names_liste

/*initiate the autocomplete function on the "myInput" element, and pass along the species array as possible autocomplete values:*/
autocomplete(document.getElementById("specieName"), availableTags);
autocomplete(document.getElementById("myInput3"), availableTags);
autocomplete(document.getElementById("myInput4"), availableTags);

