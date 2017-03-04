$(".plante").click(function () {
    var value = parseInt($(this).data("value"));
    add_node(value);
    restart();
    select_node(value);
});
$(".planteSelected").on( "click", function() {
    var value = parseInt($(this).data("value"));
    select_node(value);
});
$("#removeSelected").on( "click", function() {
    var value = parseInt($(this).data("value"));
    remove_node(value);
    restart();
});
$("#filter").on( "click", function() {
    $(this).addClass("hidden");
    $(".plante").removeClass("filtered")
});
$(".btn-filter").on( "click", function() {
    var index = $(this).data("value");
    var direction = $(this).data("direction");
    var association = $(this).data("association");
    var cur_node = graph.nodes[index];
    var $plantes =  $(".plante");
    $plantes.removeClass("filtered");
    $("#filter-name").text(cur_node.name + " " + direction + " " + association);
    $("#filter").removeClass("hidden");
    $plantes.each(function () {
        var $this = $(this);
        var thisIndex = parseInt($this.data("value"));
        var connected = graph[direction][index].filter(function (l) {
            return (l.target ? l.target : l.source) == thisIndex && l.value == association
        });
        if (connected.length == 0){
            $this.addClass("filtered")
        }
    });
});
function select_node(index) {
    $(".planteSelected").removeClass("active").each(function () {
        var $this = $(this);
        if ($this.data("value") == index) {
            $this.addClass('active')
        }
    });
    is_selected = true;
    no_transparence();
    transparent(index);
    var cur_node = graph.nodes[index];
    var $removeSelected = $("#removeSelected");
    if (cur_node.group == 5 || cur_node.group == 6 ){
        $removeSelected.addClass("hidden");
        $("#table-bug").removeClass("hidden");
        $("#table-plant").addClass("hidden")
    } else {
        $("#table-plant").removeClass("hidden");
        $("#table-bug").addClass("hidden");
        $removeSelected.removeClass("hidden");
        $removeSelected.data("value",index);
    }
    var $plantes =  $(".plante");
    $plantes.removeClass("filtered");
    $("#info-name").text(cur_node.name);
    $("#info").removeClass("hidden");

    ["forward", "backward"].forEach(function (direction) {
        associations.forEach(function (association) {
            var list_ids = $.map(graph[direction][index].filter(function (l) {
                return l.value == association
                }), function (val) {
                    return val.source ? val.source : val.target
            });
            var graph_list_ids = list_ids.filter(function (val) {
                return index_nodes.indexOf(val) > -1
                });
            $(".text", "#"+direction+"-"+association).text($.map(graph_list_ids, function (val) {
                    return " " + graph.nodes[val].name
            }));
            var $button = $(".btn", "#"+direction+"-"+association);
            $button.removeClass("hidden");
            var other_associations = list_ids.filter(function(x) {
                    return graph_list_ids.indexOf(x) < 0
                }).length;
            if (other_associations > 0 ){
                $button.data('direction', direction);
                $button.data('association', association);
                $button.data('value', index);
                if (other_associations == 1) {
                    $button.text("1 autre espèce");
                } else {
                    $button.text(String(other_associations) + " en réserve");
                }
            } else {
                $button.addClass("hidden")
            }
        });
    });
}
$(document).ready(function () {
    new Jets({
        searchTag: "#jetsPotageomeSearch",
        contentTag: "#jetsPotageomeContent"
    });
});

var svg = d3.select("svg"),
    width = +svg.attr("width"),
    height = +svg.attr("height");

var color = {
    0: "#000",
    1: "#1776b6",
    2: "#ff7f0e",
    3: "#9564bf",
    4: "#f7b6d2",
    5: "#d62728",
    6: "#24a221",
    7: "#ffe778",
    8: "#8d5649"};

var nodes = [], index_nodes = [], links = [];
var is_selected = false;
svg.append("defs").selectAll("marker")
    .data(associations)
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

var g = svg.append("g").attr("transform", "translate(" + width / 2 + "," + height / 2 + ")"),
    link = g.append("g").attr("class", "links").selectAll(".link"),
    node = g.append("g").attr("class", "nodes").selectAll(".node");

function remove_node(cur_index) {
    $("#planteSelected_" + String(cur_index), "#jetsMyPotageomeContent").addClass("hidden");
    $("#plante_" + String(cur_index), "#jetsPotageomeContent").removeClass("hidden");
    i = index_nodes.indexOf(cur_index);
    index_nodes.splice(i, 1);
    nodes.splice(i, 1);
    var cur_node = graph.nodes[cur_index];
    links = links.filter(function (l) {
        return l.source.value !== cur_node.value && l.target.value !== cur_node.value;
    });
    var to_drop = [];
    nodes.forEach(function (tmp_node) {
        if (tmp_node.group == 5 || tmp_node.group == 6) {
            if (links.filter(function (l) {
                return l.source.value == tmp_node.value || l.target.value == tmp_node.value;
            }).length == 0) {to_drop.push(tmp_node)}
        }
    });
    to_drop.forEach(function (tmp_node) {
        i = index_nodes.indexOf(tmp_node.value);
        index_nodes.splice(i, 1);
        nodes.splice(i, 1);
    })
}

function add_node(cur_index) {
    $("#plante_" + String(cur_index), "#jetsPotageomeContent").addClass("hidden");
    $("#planteSelected_" + String(cur_index), "#jetsMyPotageomeContent").removeClass("hidden");
    index_nodes.push(cur_index);
    var cur_node = graph.nodes[cur_index];
    nodes.push(cur_node);

    for (var f = 0; f < graph.forward[cur_index].length; f++) {
        var f_link = graph.forward[cur_index][f];
        if (index_nodes.indexOf(f_link.target) > -1) {
            links.push({"source": cur_node, "target": graph.nodes[f_link.target], "value": f_link.value});
        } else if (f_link.group == 5 || f_link.group == 6) {
            index_nodes.push(f_link.target);
            nodes.push(graph.nodes[f_link.target]);
            links.push({"source": cur_node, "target": graph.nodes[f_link.target], "value": f_link.value});
        }
    }
    for (var b = 0; b < graph.backward[cur_index].length; b++) {
        var b_link = graph.backward[cur_index][b];
        if (index_nodes.indexOf(b_link.source) > -1) {
            links.push({"source": graph.nodes[b_link.source], "target": cur_node, "value": b_link.value});
        } else if (b_link.group == 5 || b_link.group == 6) {
            index_nodes.push(b_link.source);
            nodes.push(graph.nodes[b_link.source]);
            links.push({"source": graph.nodes[b_link.source], "target": cur_node, "value": b_link.value});
        }
    }
}

for (var i = 0; i < list_favorable.length; i++) {
    add_node(list_favorable[i])
}
restart();

function restart() {

    // Apply the general update pattern to the nodes.
    node = node.data(nodes, function (d) {
        return d.value;
    });
    node.exit().remove();
    node = node.enter().append("g").attr("class", "node").each(function () {
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



    $(".plante").each(function () {
        var $this = $(this);
        var value = $this.data("value");
        $(".plus", $this).text(String(
            graph.forward[value].filter(function (l) {
                return index_nodes.indexOf(l.target) > -1 && l.value == "pos"
            }).length +
            graph.backward[value].filter(function (l) {
                return index_nodes.indexOf(l.source) > -1 && l.value == "pos"
            }).length
        ));
        $(".minus", $this).text(String(
            graph.forward[value].filter(function (l) {
                return index_nodes.indexOf(l.target) > -1 && l.value == "neg"
            }).length +
            graph.backward[value].filter(function (l) {
                return index_nodes.indexOf(l.source) > -1 && l.value == "neg"
            }).length
        ))
    });
    $('[data-toggle="tooltip"]').tooltip({container: "body"});
     $("circle").on( {
        mouseenter: function () {
            if (!is_selected) {
                transparent($(this).attr("value"))
            }
        },
        mouseleave: function () {
            if (!is_selected) {
                no_transparence()
            }
        },
        click: function () {
            select_node($(this).attr("value"))
        }
     });
    $("#filter").click();
    $("#info").addClass("hidden");
    is_selected = false;
    no_transparence();

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
    node.filter(function(d){ return d !== cur_node & graph.forward[index].filter(function (l) {
            return l.target == d.value
        }).length == 0 & graph.backward[index].filter(function (l) {
            return l.source == d.value
        }).length == 0})
        .transition().style("opacity", "0.12");
}

function no_transparence() {
    link.transition().style("opacity", "1");
    node.transition().style("opacity", "1");
}

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