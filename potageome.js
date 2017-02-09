$(".planteSelected").click(function (e) {
    var value = parseInt($(this).data("value"));
    remove_node(value);
});
$(document).ready(function () {
    new Jets({
        searchTag: '#jetsPotageomeSearch',
        contentTag: '#jetsPotageomeContent'
    });
});
$(".plante").click(function (e) {
    var value = parseInt($(this).data("value"));
    add_node(value);
});
var svg = d3.select("svg"),
    width = +svg.attr("width"),
    height = +svg.attr("height"),
    color = d3.scaleOrdinal(d3.schemeCategory10);

var nodes = [], index_nodes = [];
links = [];

var simulation = d3.forceSimulation(nodes)
    .force("charge", d3.forceManyBody().strength(-1000))
    .force("link", d3.forceLink(links).distance(200))
    .force("x", d3.forceX())
    .force("y", d3.forceY())
    .alphaTarget(1)
    .on("tick", ticked);

var g = svg.append("g").attr("transform", "translate(" + width / 2 + "," + height / 2 + ")"),
    link = g.append("g").attr("stroke", "#000").attr("stroke-width", 1.5).selectAll(".link"),
    node = g.append("g").attr("stroke", "#fff").attr("stroke-width", 1.5).selectAll(".node");

function remove_node(cur_index) {
    $("#planteSelected_" + String(cur_index), "#jetsMyPotageomeContent").hide().addClass('active');
    $("#plante_" + String(cur_index), "#jetsPotageomeContent").show().removeClass('active');
    i = index_nodes.indexOf(cur_index);
    index_nodes.splice(i, 1);
    nodes.splice(i, 1);
    var cur_node = graph.nodes[cur_index];
    links = links.filter(function (l) {
        return l.source !== cur_node && l.target !== cur_node;
    });
    restart();
}

function add_node(cur_index) {
    $("#plante_" + String(cur_index), "#jetsPotageomeContent").hide().removeClass('active');
    $("#planteSelected_" + String(cur_index), "#jetsMyPotageomeContent").show().addClass('active');
    index_nodes.push(cur_index);
    var cur_node = graph.nodes[cur_index];
    nodes.push(cur_node);
    for (var j = 0; j < graph.links.length; j++) {
        var cur_link = graph.links[j];
        if (cur_link.source == cur_index && index_nodes.indexOf(cur_link.target) > -1) {
            links.push({"source": cur_node, "target": graph.nodes[cur_link.target], "value": cur_link.value});
        } else if (cur_link.target == cur_index && index_nodes.indexOf(cur_link.source) > -1) {
            links.push({"source": cur_node, "target": graph.nodes[cur_link.target], "value": cur_link.value});
        }
    }
    restart();
}

for (var i = 0; i < list_favorable.length; i++) {
    var cur_index = list_favorable[i];
    add_node(cur_index)
}


function restart() {

    // Apply the general update pattern to the nodes.
    node = node.data(nodes, function (d) {
        return d.id;
    });
    node.exit().remove();
    node = node.enter().append("circle").attr("fill", function (d) {
        return color(d.group);
    }).attr("r", 8).merge(node);

    // Apply the general update pattern to the links.
    link = link.data(links, function (d) {
        return d.source.id + "-" + d.target.id;
    });
    link.exit().remove();
    link = link.enter().append("line").merge(link);

    // Update and restart the simulation.
    simulation.nodes(nodes);
    simulation.force("link").links(links);
    simulation.alpha(1).restart();
}

function ticked() {
    node.attr("cx", function (d) {
        return d.x;
    })
        .attr("cy", function (d) {
            return d.y;
        });

    link.attr("x1", function (d) {
        return d.source.x;
    })
        .attr("y1", function (d) {
            return d.source.y;
        })
        .attr("x2", function (d) {
            return d.target.x;
        })
        .attr("y2", function (d) {
            return d.target.y;
        });
}