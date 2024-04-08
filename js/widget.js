import * as d3 from "https://cdn.jsdelivr.net/npm/d3@6/+esm";
import { BarChart } from "./barchart.js";
import "./widget.css";

function render({ model, el }) {
  let div = document.createElement("div");
  div.id = "my_dataviz";

  let data = d3.csvParse(model.get("data"));
  let x = model.get("x");
  let selection = model.get("selection");

  let barchart = new BarChart(div, data, x);
  el.appendChild(div);

  if (data.columns[selection] == x) {
    selection = data.columns[selection + 1];
  }

  model.on("msg:custom", (msg) => {
    // on dropdown menu selection change
    if (msg.type === "update-selection") {
      let newSelection = msg.value;
      let myValue = data.columns[newSelection];
      barchart.update(myValue);
    }
  });

  setTimeout(() => {
    barchart.init();
    barchart.update(selection);
  }, 100);
}

export default { render };
