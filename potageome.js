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
            links.push({"source": graph.nodes[cur_link.source], "target": cur_node, "value": cur_link.value});
        }
    }
    restart();
}

for (var i = 0; i < list_favorable.length; i++) {
    add_node(list_favorable[i])
}


function restart() {

    // Apply the general update pattern to the nodes.
    node = node.data(nodes, function (d) {
        return d.id;
    });
    node.exit().remove();
    node = node.enter().append("g").each(function(d) {
        d3.select(this).insert("circle").attr("fill", function (d) {
            return color(d.group);
        }).attr("r", 10);
        d3.select(this).insert("text")
          .attr("x", 11).attr("y", -4)
            .text(function(d) { return d.name; })
    }).merge(node);

    // Apply the general update pattern to the links.
    link = link.data(links, function (d) {
        return d.source.id + "-" + d.target.id;
    });
    link.exit().remove();
    link = link.enter().append("path")
        .attr("class", function (d) {
            return "link " + d.value;
        })
        .attr("marker-end", function (d) {
            return "url(#" + d.value + ")";
        }).merge(link);

    // Update and restart the simulation.
    simulation.nodes(nodes);
    simulation.force("link").links(links);
    simulation.alpha(1).restart();
}


function tick() {
    node.attr("transform", function (d) {
        return "translate("+d.x +"," + d.y + ")";
    });

    link.attr("d", function (d) {
        var dx = d.target.x - d.source.x,
            dy = d.target.y - d.source.y,
            dr = Math.sqrt(dx * dx + dy * dy);
        return "M" + d.source.x + "," + d.source.y + "A" + dr + "," + dr + " 0 0,1 " + d.target.x + "," + d.target.y;
    })
}