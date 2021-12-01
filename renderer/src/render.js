const mjml2html = require("mjml");
const Vue = require("vue");
const fs = require("fs");

const app = new Vue({
  data: {
    logo: "Zażółć gęślą jaźń",
  },
  template: `
  <mj-section>
    <mj-column>
      <mj-text font-size="20px" color="#F45E43" font-family="helvetica">{{ logo }}</mj-text>
    </mj-column>
  </mj-section>`,
});

const renderer = require("vue-server-renderer").createRenderer({
  template: `
    <mjml>
      <mj-body>
        <!--vue-ssr-outlet-->
      </mj-body>
    </mjml>`,
});

const getCurrentDate = () => new Date(Date.now()).toISOString().split("T")[0];

renderer.renderToString(app).then((html) => {
  const htmlWithoutDataServerRenderedAttribute = html.replace(
    `data-server-rendered="true"`,
    ""
  );
  const plainHtml = mjml2html(htmlWithoutDataServerRenderedAttribute);
  fs.writeFile(
    `output_${getCurrentDate()}.html`,
    plainHtml.html,
    function (err, data) {
      if (err) {
        return console.log(err);
      }
      console.log(
        `Generated the file output_${getCurrentDate()}.html. ${data}`
      );
    }
  );
});
