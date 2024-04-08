import * as d3 from "https://cdn.jsdelivr.net/npm/d3@6/+esm";
import { BarChart } from "./barchart.js";
import "./widget.css";

function render({ model, el }) {
  console.log("rendering the widget 29");
  let div = document.createElement("div");
  div.id = "my_dataviz";

  let data = d3.csvParse(model.get("data"));
  let x = model.get("x");
  let barchart = new BarChart(div, data, x);
  el.appendChild(div);

  let item = data.columns[0];
  if (data.columns[0] == x) {
    item = data.columns[1];
  }

  setTimeout(() => {
    barchart.init();
    barchart.update(item);
  }, 100);
}

export default { render };
