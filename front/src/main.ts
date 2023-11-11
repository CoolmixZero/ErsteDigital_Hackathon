import { createApp } from "vue";
import App from "./App.vue";
import PrimeVue from "primevue/config";
import Menubar from "primevue/menubar";
import Avatar from "primevue/avatar";
import Button from "primevue/button";
import DataTable from "primevue/datatable";
import Column from "primevue/column";
import Menu from "primevue/menu";
import InputText from "primevue/inputtext";
import Message from "primevue/message";
import axios from "axios";
import VueAxios from "vue-axios";
import VueWriter from "vue-writer";
import TabView from "primevue/tabview";
import TabPanel from "primevue/tabpanel";

import "./style.scss";

import "primevue/resources/themes/lara-light-blue/theme.css";
import "primeicons/primeicons.css";

const app = createApp(App);
app.use(PrimeVue, { ripple: true });
app.use(VueAxios, axios);
app.component("Button", Button);
app.component("Menubar", Menubar);
app.component("Avatar", Avatar);
app.component("Menu", Menu);
app.component("DataTable", DataTable);
app.component("Column", Column);
app.component("InputText", InputText);
app.component("Message", Message);
app.component("TabView", TabView);
app.component("TabPanel", TabPanel);
app.use(VueWriter);
app.mount("#app");
