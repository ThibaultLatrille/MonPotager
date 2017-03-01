$(".planteSelected").on( "click", function() {
    var value = parseInt($(this).data("value"));
    remove_node(value);
    restart();
});
$("#filter").on( "click", function() {
    $(this).hide();
    $(".plante").removeClass("btn-success").removeClass("btn-danger").removeClass("filtered").addClass("btn-default")
});
$(document).ready(function () {
    new Jets({
        searchTag: "#jetsPotageomeSearch",
        contentTag: "#jetsPotageomeContent"
    });
});
$(".plante").click(function () {
    var value = parseInt($(this).data("value"));
    add_node(value);
    restart();
});
var svg = d3.select("svg"),
    width = +svg.attr("width"),
    height = +svg.attr("height"),
    color = d3.scaleOrdinal(d3.schemeCategory10);

var nodes = [], index_nodes = [], links = [];

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
    link = g.append("g").selectAll(".link"),
    node = g.append("g").selectAll(".node");

function remove_node(cur_index) {
    $("#planteSelected_" + String(cur_index), "#jetsMyPotageomeContent").hide().addClass("active");
    $("#plante_" + String(cur_index), "#jetsPotageomeContent").show().removeClass("active");
    i = index_nodes.indexOf(cur_index);
    index_nodes.splice(i, 1);
    nodes.splice(i, 1);
    var cur_node = graph.nodes[cur_index];
    for (var f = 0; f < graph.forward[cur_index].length; f++) {
        var f_link = graph.forward[cur_index][f];
        if (f_link.group == 5 || f_link.group == 6) {
            var inter = $(index_nodes).filter($.map(graph.backward[f_link.target], function (val) {
                return val.source
            }));
            if (inter.length == 0) {
                i = index_nodes.indexOf(f_link.target);
                index_nodes.splice(i, 1);
                nodes.splice(i, 1);
            }
        }
    }
    links = links.filter(function (l) {
        return l.source !== cur_node && l.target !== cur_node;
    });
}

function add_node(cur_index) {
    $("#plante_" + String(cur_index), "#jetsPotageomeContent").hide().removeClass("active");
    $("#planteSelected_" + String(cur_index), "#jetsMyPotageomeContent").show().addClass("active");
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
    node = node.enter().append("g").each(function () {
        d3.select(this).insert("circle")
            .attr("fill", function (d) {
                return color(d.group)
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
    $("circle").on( "click", function() {
        var index = $(this).attr("value");
        var $plantes =  $(".plante");
        $plantes.removeClass("filtered");
        $("#filter-name").text(graph.nodes[index].name);
        $("#filter").show();
        $plantes.each(function () {
            var $this = $(this);
            var thisIndex = parseInt($this.data("value"));
            var connected = graph.forward[index].filter(function (l) {
                return l.target == thisIndex
            });
            if (connected.length == 0){
                $this.addClass("filtered")
            } else if (connected[0].value == "pos") {
                $this.removeClass("btn-default").addClass("btn-success")
            } else if (connected[0].value == "neg") {
                $this.removeClass("btn-default").addClass("btn-danger")
            }
        });
    });
    // Update and restart the simulation.
    simulation.nodes(nodes);
    simulation.force("link").links(links);
    simulation.alpha(1).restart();
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