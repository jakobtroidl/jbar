import * as d3 from "https://cdn.jsdelivr.net/npm/d3@6/+esm";

export class BarChart {
  constructor(parent, data, x) {
    this.data = data;
    this.parent = parent;
    this.category = x;
  }

  init() {
    // console.log('initialize the chart');

    // set the dimensions and margins of the graph
    const margin = { top: 30, right: 30, bottom: 70, left: 60 };
    this.width = this.parent.clientWidth - margin.left - margin.right;
    this.height = 500 - margin.top - margin.bottom;

    let parentTag = "#" + this.parent.id;
    this.svg = d3
      .select(parentTag)
      .append("svg")
      .attr("width", this.width + margin.left + margin.right)
      .attr("height", this.height + margin.top + margin.bottom)
      .append("g")
      .attr("transform", `translate(${margin.left},${margin.top})`);

    this.x = d3.scaleBand().range([0, this.width]).padding(0.2);
    this.xAxis = this.svg
      .append("g")
      .attr("transform", `translate(0,${this.height})`);

    // Initialize the Y axis
    this.y = d3.scaleLinear().range([this.height, 0]);
    this.yAxis = this.svg.append("g").attr("class", "myYaxis");
  }

  update(variableName) {
    this.x.domain(this.data.map((d) => d[this.category]));
    this.xAxis.transition().duration(1000).call(d3.axisBottom(this.x));

    // update the chart
    this.y.domain([0, d3.max(this.data, (d) => +d[variableName])]);
    this.yAxis.transition().duration(1000).call(d3.axisLeft(this.y));

    const u = this.svg.selectAll("rect").data(this.data);

    // update bars
    u.join("rect")
      .transition()
      .duration(1000)
      .attr("x", (d) => this.x(d[this.category]))
      .attr("y", (d) => this.y(d[variableName]))
      .attr("width", this.x.bandwidth())
      .attr("height", (d) => this.height - this.y(d[variableName]))
      .attr("fill", "#69b3a2");

    d3.selectAll("rect")
      .on("mouseover", function (d) {
        d3.select(this).style("fill", "orange");
      })
      .on("mouseout", function (d) {
        d3.select(this).style("fill", "#69b3a2"); // Assume 'steelblue' is the original color
      });
  }
}
