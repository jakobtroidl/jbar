import * as d3 from "https://cdn.jsdelivr.net/npm/d3@6/+esm";
import { BarChart } from "./barchart.js";

function render({ model, el }) {
  let div = document.createElement("div");
  div.id = "my_dataviz";

  let data = d3.csvParse(model.get("data"));

  let category = model.get("x");
  // 0 is category, pick first value after category as default
  let selection = data.columns[1];

  let barchart = new BarChart(div, data, category);
  el.appendChild(div);

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
