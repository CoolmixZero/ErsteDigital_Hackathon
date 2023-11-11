<script setup>
import { ref } from "vue";

let month = ref(null);
let money = ref(null);

const items = ref([
  {
    label: "Home",
    icon: "pi pi-home",
  },
  {
    label: "Profile",
    icon: "pi pi-user",
  },
  {
    label: "Send Money",
    icon: "pi pi-arrow-up",
  },
  {
    label: "My consultant",
    icon: "pi pi-envelope",
  },
]);

const categories = [
  "Coffee Shop",
  "Clothing Store",
  "Restaurant",
  "Gym",
  "Supermarket",
  "Movie Theater",
  "Gas Station",
  "Pharmacy",
  "Bookstore",
  "Hair Salon",
  // Add more categories as needed
];

const dummyData = [];

for (let i = 0; i < 25; i++) {
  const randomCategory = categories[Math.floor(Math.random() * categories.length)];
  const randomAmount = Math.floor(Math.random() * 100); // Generate a random amount (you can adjust the range)
  const randomBalance = Math.floor(Math.random() * 1000); // Generate a random balance (you can adjust the range)

  dummyData.push({
    category: randomCategory,
    amount: new Intl.NumberFormat("de-DE", { style: "currency", currency: "EUR" }).format(randomAmount),
    balance: new Intl.NumberFormat("de-DE", { style: "currency", currency: "EUR" }).format(randomBalance),
  });
}

const rows = ref(dummyData);
</script>

<script>
import * as echarts from "echarts";
import { nextTick } from "vue";

export default {
  name: "App",

  data() {
    return {
      aiCalled: false,
    };
  },

  methods: {
    CallAiAssistance() {
      this.aiCalled = true;

      this.axios.get("localhost:3000/assistant").then((response) => {
        console.log(response.data);
      });

      nextTick(() => {
        this.initChart();
      });
    },
    initChart() {
      const myChart = echarts.init(this.$refs.lineChart);

      // Sample data for the line chart
      const data = {
        xData: ["Jan", "Feb", "Mar", "Apr", "May"],
        yData: [50, 60, 70, 80, 90],
      };

      const option = {
        grid: {
          top: 20,
        },
        xAxis: {
          type: "category",
          data: data.xData,
          axisLine: {
            lineStyle: {
              color: "#999", // X-axis line color
            },
          },
        },
        yAxis: {
          type: "value",
          axisLine: {
            lineStyle: {
              color: "#999", // Y-axis line color
            },
          },
        },
        series: [
          {
            type: "line",
            data: data.yData,
            lineStyle: {
              color: "lightblue", // Light blue line color
              width: 3, // Increase line thickness
            },
            itemStyle: {
              color: "lightblue", // Data point color
            },
            label: {
              show: true,
              position: "top",
              textStyle: {
                color: "#333", // Label text color
              },
            },
            areaStyle: {
              // Add a gradient below the line
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                {
                  offset: 0,
                  color: "rgba(173, 216, 230, 0.8)", // Gradient color at the top
                },
                {
                  offset: 1,
                  color: "rgba(255, 255, 255, 0.2)", // Gradient color at the bottom
                },
              ]),
            },
            symbol: "circle", // Use circles as markers
            symbolSize: 8, // Set marker size
            tooltip: {
              trigger: "axis",
              formatter: "{b}: {c}", // Display x-axis label and y-axis value in tooltip
            },
          },
        ],
      };

      myChart.setOption(option);
    },
  },
};
</script>

<template>
  <div class="bank-container flex flex-col w-full">
    <Menubar :model="items" class="shadow-lg w-full">
      <template #start>
        <img src="./assets/logo.png" style="width: 120px" class="mr-3" alt="" />
      </template>

      <template #item="{ item, props }">
        <a v-ripple class="flex items-center" v-bind="props.action">
          <span :class="item.icon" />
          <span class="ml-2">{{ item.label }}</span>
        </a>
      </template>

      <template #end>
        <div class="flex items-center gap-4 font-semibold text-lg">
          <span>$251,765</span>
          <Avatar image="https://thispersondoesnotexist.com/" size="large" shape="circle" />
        </div>
      </template>
    </Menubar>

    <div class="h-full w-full mt-5 flex flex-row gap-5">
      <div class="sidebar w-2/6 h-full flex flex-col gap-5">
        <div class="card h-80">
          <div class="front-side absolute w-full h-full rounded-xl bg-white">
            <div class="background absolute w-full h-full"></div>
            <div class="title mt-6 ml-6 font-bold text-slate-700 text-xl">ERSTE Credit Card</div>
            <div class="card-number mt-24 ml-6 font-bold text-slate-700 text-xl">4405 1235 6534 3217</div>
          </div>
        </div>
        <div class="sidebar-data shadow-lg bg-white rounded-lg h-full">
          <Menu
            class="w-full"
            :model="[
              {
                label: 'Documents',
                items: [
                  {
                    label: 'Top up',
                    icon: 'pi pi-arrow-up',
                  },
                  {
                    label: 'Send',
                    icon: 'pi pi-arrow-down',
                  },
                ],
              },
              {
                label: 'Profile',
                items: [
                  {
                    label: 'Settings',
                    icon: 'pi pi-cog',
                  },
                  {
                    label: 'Information',
                    icon: 'pi pi-info',
                  },
                  {
                    label: 'Contracts',
                    icon: 'pi pi-file',
                  },

                  {
                    label: 'Logout',
                    icon: 'pi pi-sign-out',
                  },
                ],
              },
            ]"
          />
        </div>
      </div>

      <div class="main-content w-full h-full shadow-lg bg-white rounded-lg">
        <div class="p-7 flex flex-col items-center">
          <Message v-if="aiCalled" :closable="false" class="w-full" icon="pi pi-star">
            <VueWriter
              :typeSpeed="10"
              :array="[
                `Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.`,
              ]"
              :iterations="1"
            />
          </Message>

          <span class="text-2xl font-bold self-start">Spendings & Incomes</span>

          <DataTable :value="rows" scrollable scrollHeight="400px" class="mt-5 self-start w-full" tableStyle="max-height: 200px;">
            <Column field="category" header="Category"></Column>
            <Column field="amount" header="Amount"></Column>
            <Column field="balance" header="Balance"></Column>
          </DataTable>

          <template v-if="!aiCalled">
            <span class="text-2xl font-bold mt-7">Ask AI assistant! ✨</span>

            <div class="flex flex-row mt-6 gap-3">
              <span class="p-input-icon-left">
                <i class="pi pi-money-bill" />
                <InputText v-model="money" placeholder="How much to save" />
              </span>
              <span class="p-input-icon-left">
                <i class="pi pi-clock" />
                <InputText v-model="month" placeholder="Month to save" />
              </span>
              <Button @click="CallAiAssistance" class="ai-button" label="Submit" icon="pi pi-reddit" />
              <Button icon="pi pi-microphone" rounded />
            </div>
          </template>

          <template v-else>
            <span class="text-2xl font-bold mt-7">Account Balance AI prediction</span>
            <div ref="lineChart" class="echarts-chart"></div>
          </template>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.sidebar {
  .card {
    position: relative;
    .front-side {
      overflow: hidden;
      .background {
        background-image: url(https://media.istockphoto.com/id/472297015/vector/money-business-finance-and-real-estate-background-pattern.jpg?s=612x612&w=0&k=20&c=PnvrG4KNlm3Xg8A1_SV4QRwtPio4umh1EgFPhdNw__s=);
        background-size: cover;
        background-position: center;
        opacity: 0.5;
      }

      .title,
      .card-number {
        color: #172c66;
        z-index: 2;
        position: relative;
      }
    }
  }
}

.main-content {
  max-height: 680px;
  overflow: auto;

  .echarts-chart {
    width: 100%;
    height: 400px;
  }
}
</style>
