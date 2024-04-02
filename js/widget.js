// import * as d3 from "https://cdn.jsdelivr.net/npm/d3@6/+esm";
// import { BarChart } from "./barchart.js";
import "./widget.css";

function render({ model, el }) {
  console.log("rendering the widget 5");
  // let div = document.createElement("div");
  // div.id = "my_dataviz";

  // let data = d3.csvParse(model.get("data"));
  // let barchart = new BarChart(div, data);

  // let button1 = document.createElement("button");
  // button1.innerHTML = `outgoing_syn`;
  // button1.addEventListener("click", () => {
  //   barchart.update("outgoing_syn");
  // });
  // el.appendChild(button1);

  // let button2 = document.createElement("button");
  // button2.innerHTML = `incoming_syn`;
  // button2.addEventListener("click", () => {
  //   barchart.update("incoming_syn");
  // });
  // el.appendChild(button2);

  // el.appendChild(div);

  // console.log("barchart", barchart);

  // barchart.init();
  // barchart.update("outgoing_syn");
}

export default { render };
