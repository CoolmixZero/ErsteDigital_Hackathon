import { createApp } from "vue";
import App from "./App.vue";
import PrimeVue from "primevue/config";
import Menubar from "primevue/menubar";
import Avatar from "primevue/avatar";
import Button from "primevue/button";
import TabView from "primevue/tabview";
import TabPanel from "primevue/tabpanel";
import Menu from "primevue/menu";

import "./style.scss";

import "primevue/resources/themes/lara-light-blue/theme.css";
import "primeicons/primeicons.css";

const app = createApp(App);
app.use(PrimeVue, { ripple: true });
app.component("Button", Button);
app.component("Menubar", Menubar);
app.component("Avatar", Avatar);
app.component("Menu", Menu);
app.component("TabView", TabView);
app.component("TabPanel", TabPanel);
app.mount("#app");
