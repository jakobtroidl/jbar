import "./widget.css";
import * as d3 from "https://cdn.jsdelivr.net/npm/d3@6/+esm";

function render({ model, el }) {
  let data = d3.csvParse(model.get("data"));

  // create a div for the first chart
  let button1 = document.createElement("button");
  button1.innerHTML = `outgoing_syn`;
  button1.addEventListener("click", () => {
    update("outgoing_syn");
  });
  el.appendChild(button1);

  let button2 = document.createElement("button");
  button2.innerHTML = `incoming_syn`;
  button2.addEventListener("click", () => {
    update("incoming_syn");
  });
  el.appendChild(button2);

  // create div for the chart
  let div = document.createElement("div");
  div.id = "my_dataviz";
  el.appendChild(div);

  // set the dimensions and margins of the graph
  const margin = { top: 30, right: 30, bottom: 70, left: 60 },
    width = div.clientWidth - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

  // append the svg object to the body of the page
  const svg = d3
    .select("#my_dataviz")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", `translate(${margin.left},${margin.top})`);

  // Initialize the X axis
  const x = d3.scaleBand().range([0, width]).padding(0.2);
  const xAxis = svg.append("g").attr("transform", `translate(0,${height})`);

  // Initialize the Y axis
  const y = d3.scaleLinear().range([height, 0]);
  const yAxis = svg.append("g").attr("class", "myYaxis");

  // Initialize plot
  update("outgoing_syn", data);

  // A function that create / update the plot for a given variable:
  function update(selectedVar) {
    // X axis
    x.domain(data.map((d) => d.cell_type));
    xAxis.transition().duration(1000).call(d3.axisBottom(x));

    // Add Y axis
    y.domain([0, d3.max(data, (d) => +d[selectedVar])]);
    yAxis.transition().duration(1000).call(d3.axisLeft(y));

    // variable u: map data to existing bars
    const u = svg.selectAll("rect").data(data);

    // update bars
    u.join("rect")
      .transition()
      .duration(1000)
      .attr("x", (d) => x(d.cell_type))
      .attr("y", (d) => y(d[selectedVar]))
      .attr("width", x.bandwidth())
      .attr("height", (d) => height - y(d[selectedVar]))
      .attr("fill", "#69b3a2");
  }
}

export default { render };
