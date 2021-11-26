const mjml2html = require("mjml");
const Vue = require("vue");
const fs = require("fs");

const app = new Vue({
  data: {
    logo: "mojeanalizy.pl",
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

renderer.renderToString(app).then((html) => {
  const htmlWithoutDataServerRenderedAttribute = html.replace(
    `data-server-rendered="true"`,
    ""
  );
  const plainHtml = mjml2html(htmlWithoutDataServerRenderedAttribute);
  fs.writeFile("example.html", plainHtml.html, function (err, data) {
    if (err) {
      return console.log(err);
    }
    console.log(data);
  });
});
