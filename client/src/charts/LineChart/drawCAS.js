import * as d3 from 'd3';
import _ from 'lodash';

const draw = (props) => {
    let data = [];
    if (props.data !== null) {
        data = _.cloneDeep(props.data);
    }
    d3.select('.linechart-cas > *').remove();
    let margin = { top: 20, right: 50, bottom: 60, left: 40 }
    const width = props.width - margin.left - margin.right;
    const height = props.height - margin.top - margin.bottom;
    let svg = d3.select(".linechart-cas")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform",
            "translate(" + margin.left + "," + margin.top + ")");

    data.forEach(function (d) {
        console.log(d);
        d.source_date = d3.timeParse("%Y-%m-%d")(d.source_date);
        d.value = +d.value;
    });

    var xExtent = d3.extent(data, function(d) { return d.source_date; }),
        xRange = xExtent[1] - xExtent[0];
    
    var x = d3.scaleTime().range([0, width]);
    x.domain(d3.extent(data, function(d) { return d.source_date; }));

    var y = d3.scaleLinear().range([height, 0]);
    y.domain([d3.min(data, function(d) { return d.value; }) - 5, 60]);
    svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x)
              .tickFormat(d3.timeFormat("%Y-%m-%d")).tickValues(data.map(d=>d.source_date)))
      .selectAll("text")	
        .style("text-anchor", "end")
        .attr("dx", "-.8em")
        .attr("dy", ".15em")
        .attr("transform", "rotate(-65)");

    svg.append("g")
        .call(d3.axisLeft(y));

    // Add the line
    svg.append("path")
        .datum(data)
        .attr("fill", "none")
        .attr("stroke", "steelblue")
        .attr("stroke-width", 1.5)
        .attr("d", d3.line()
            .x(function (d) { return x(d.source_date) })
            .y(function (d) { return y(d.value) })
        )

    svg.selectAll(".dot")
        .data(data)
        .enter()
        .append("circle")
        .attr("class", "dot")
        .attr("cx", function(d) { return x(d.source_date) })
        .attr("cy", function(d) { return y(d.value) })
        .attr("r", 5);

    svg.selectAll(".text")
        .data(data)
        .enter()
        .append("text")
        .attr("class", "label")
        .attr("x", function(d, i) { return x(d.source_date) })
        .attr("y", function(d) { return y(d.value) })
        .attr("dy", "-10")
        .text(function(d) {return d.value; });
}

export default draw;