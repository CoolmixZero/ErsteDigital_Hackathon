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

const dummyData = [
  ["2023-01-01", "Groceries", -45],
  ["2023-01-01", "Utilities", -30],
  ["2023-01-02", "Rent", -250],
  ["2023-01-02", "Freelance Income", 200],
  ["2023-01-03", "Transport", -20],
  ["2023-01-04", "Dining Out", -35],
  ["2023-01-05", "Gym Membership", -25],
  ["2023-01-05", "Salary", 1000],
  ["2023-01-06", "Entertainment", -50],
  ["2023-01-07", "Groceries", -60],
  ["2023-01-08", "Healthcare", -40],
  ["2023-01-09", "Transport", -15],
  ["2023-01-10", "Utilities", -25],
  ["2023-01-11", "Clothing", -75],
  ["2023-01-12", "Freelance Income", 150],
  ["2023-01-13", "Rent", -250],
  ["2023-01-14", "Groceries", -55],
  ["2023-01-15", "Dining Out", -30],
  ["2023-01-16", "Gym Membership", -25],
  ["2023-01-18", "Entertainment", -60],
  ["2023-01-19", "Groceries", -70],
  ["2023-01-20", "Healthcare", -45],
  ["2023-01-21", "Transport", -20],
  ["2023-01-22", "Utilities", -30],
  ["2023-01-23", "Clothing", -80],
  ["2023-01-24", "Freelance Income", 250],
  ["2023-01-25", "Rent", -250],
  ["2023-01-26", "Groceries", -65],
  ["2023-01-27", "Dining Out", -40],
  ["2023-01-28", "Gym Membership", -25],
  ["2023-01-30", "Entertainment", -55],
  ["2023-01-31", "Groceries", -75],
  ["2023-01-31", "Healthcare", -50],
  ["2023-02-01", "Transport", -25],
  ["2023-02-02", "Utilities", -35],
  ["2023-02-03", "Clothing", -90],
  ["2023-02-04", "Freelance Income", 300],
  ["2023-02-05", "Rent", -275],
  ["2023-02-06", "Groceries", -50],
  ["2023-02-07", "Dining Out", -45],
  ["2023-02-08", "Gym Membership", -30],
  ["2023-02-09", "Salary", 1150],
  ["2023-02-10", "Entertainment", -70],
  ["2023-02-11", "Groceries", -80],
  ["2023-02-12", "Healthcare", -60],
  ["2023-02-13", "Transport", -30],
  ["2023-02-14", "Utilities", -40],
  ["2023-02-15", "Clothing", -100],
];

const modifiedData = [];

for (let i = 0; i < dummyData.length; i++) {
  // const randomCategory = categories[Math.floor(Math.random() * categories.length)];
  // const randomAmount = Math.floor(Math.random() * 100); // Generate a random amount (you can adjust the range)
  const randomBalance = 1000;

  modifiedData.push({
    category: dummyData[i][1],
    amount: new Intl.NumberFormat("de-DE", { style: "currency", currency: "EUR" }).format(dummyData[i][2]),
    balance: new Intl.NumberFormat("de-DE", { style: "currency", currency: "EUR" }).format(randomBalance + dummyData[i][2]),
  });
}

const rows = ref(modifiedData);
</script>

<script>
import * as echarts from "echarts";
import { nextTick } from "vue";

export default {
  name: "App",

  data() {
    return {
      aiCalled: false,
      responseData: null,
      loader: false,
      showReceiptResults: false,
    };
  },

  methods: {
    CallAiAssistance() {
      this.aiCalled = true;

      this.axios.get("http://127.0.0.1:3000/forecast").then((response) => {
        // Parse the JSON string into a JavaScript object
        const parsedData = JSON.parse(response.data);

        // Store the parsed data
        this.responseData = {
          xData: Object.values(parsedData.ds),
          yData: Object.values(parsedData.y),
          predictedYData: Object.values(parsedData.yhat),
        };
        nextTick(() => {
          this.initChart();
        });
      });
    },
    initChart() {
      const myChart = echarts.init(this.$refs.lineChart);

      // Sample data for the line chart
      const data = {
        xData: this.responseData.xData,
        yData: this.responseData.yData,
        predictedYData: this.responseData.predictedYData,
      };

      console.log(data);

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
              show: false,
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
          {
            type: "line",
            data: data.predictedYData,
            lineStyle: {
              color: "lightgreen", // Light blue line color
              width: 3, // Increase line thickness
            },
            itemStyle: {
              color: "lightgreen", // Data point color
            },
            label: {
              show: false,
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
    onAdvancedUpload(event) {
      console.log(event);
      this.loader = true;
      setTimeout(this.finishLoading, 2000);
    },
    finishLoading() {
      this.showReceiptResults = true;
      this.loader = false;
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
          <span>$5,000</span>
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
        <TabView>
          <TabPanel header="AI Assistant">
            <div class="flex flex-col items-center">
              <Message v-if="aiCalled" :closable="false" class="w-full" icon="null">
                Looking at your transaction history, here are the categories where you can save money: <br /><br /><b>1. Groceries: </b><br />You
                spent a total of <b>$660</b> on groceries. You can save money in this category by planning your meals, making a grocery list, and
                avoiding impulse purchases. Consider buying in bulk or shopping at budget-friendly stores to save even more. <br /><br /><b
                  >2. Dining Out: </b
                >You spent a total of <b>$150</b> on dining out. To save money in this category, you can try cooking at home more often and reserve
                eating out for special occasions. <br /><br /><b>3. Gym Membership:</b> You spent a total of <b>$105</b> on your gym membership. To
                save money, you could explore alternative fitness options such as outdoor activities, home workouts, or joining a local community
                center that offers affordable fitness programs. <br /><br /><b>4. Utilities:</b> You spent a total of <b>$95</b> on utilities. To save
                money in this category, you can conserve energy by turning off lights and appliances when not in use, adjusting your thermostat, and
                using energy-efficient products. <br /><br /><b>5. Transportation:</b> You spent a total of <b>$95</b> on transportation. To save
                money in this category, consider carpooling, using public transportation, biking, or walking for shorter distances whenever possible.
                Additionally, monitoring gas prices and planning your routes efficiently can help reduce expenses. <br /><br /><b>6. Clothing:</b> You
                spent a total of <b>$345</b> on clothing. To save money, assess your wardrobe and prioritize buying essential items only. Consider
                shopping during sales, buying second-hand, or swapping clothes with friends or family. <br /><br /><b>7. Healthcare:</b> You spent a
                total of <b>$145</b> on healthcare expenses. While healthcare is essential, you can save money in this category by exploring options
                like generic medications, preventive care, and comparing prices for medical services and prescriptions. By making adjustments in these
                categories, you can potentially save around <b>$1560 in total</b>. Remember, small changes in daily habits can add up to significant
                savings over time.
              </Message>

              <span class="text-2xl font-bold self-start">Spendings & Incomes</span>

              <DataTable :value="rows" scrollable scrollHeight="400px" class="mt-5 self-start w-full" tableStyle="max-height: 200px;">
                <Column field="category" header="Category"></Column>
                <Column field="amount" header="Amount">
                  <template #body="props">
                    <span :class="props.data.amount.includes('-') ? 'text-red-500' : 'text-green-500'">
                      {{ props.data.amount }}
                    </span>
                  </template>
                </Column>
                <Column field="balance" header="Balance">
                  <template #body="props">
                    <span :class="props.data.amount.includes('-') ? 'text-red-500' : 'text-green-500'">
                      {{ props.data.balance }}
                    </span>
                  </template>
                </Column>
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
                  <Button @click="CallAiAssistance" class="ai-button" label="Submit" icon="pi pi-reddit" /></div
              ></template>

              <template v-else>
                <span class="text-2xl font-bold mt-7">Account Balance AI prediction</span>
                <div ref="lineChart" class="echarts-chart"></div>
              </template>
            </div>
          </TabPanel>
          <TabPanel header="Receipt AI Reader">
            <div class="flex flex-col items-center">
              <div class="text-2xl font-bold mt-4 mb-4 self-start">Upload your receipt! ✨</div>

              <div class="w-full">
                <FileUpload name="demo[]" url="/api/upload" @select="onAdvancedUpload($event)" :multiple="true" accept="image/*">
                  <template #empty>
                    <p>Drag and drop files to here to upload.</p>
                  </template>
                </FileUpload>
              </div>

              <ProgressSpinner v-if="loader" class="mt-8" />

              <Message v-if="showReceiptResults" :closable="false" class="w-full text-xl" icon="null">
                <h2>Items:</h2>
                <ol class="text-xl">
                    <li>Zucchini Green: 0.778kg @ $5.99/kg</li>
                    <li>Banana Cavendish: 0.442kg @ $2.99/kg</li>
                    <li>Special (no details provided)</li>
                    <li>Special (no details provided)</li>
                    <li>Potatoes Brushed: 1.328kg @ $2.99/kg</li>
                    <li>Broccoli: 0.808kg @ $5.99/kg</li>
                    <li>Brussel Sprouts: 0.322kg @ $15.99/kg</li>
                    <li>Special (no details provided)</li>
                    <li>Grapes Green: 1.174kg @ $5.99/kg</li>
                    <li>Peas Snow: 0.218kg @ $14.99/kg</li>
                    <li>Tomatoes Grape</li>
                    <li>Lettuce Iceberg</li>
                </ol>

                <h2>Subtotals:</h2>
                <ul class="text-xl">
                    <li>$4.66</li>
                    <li>$1.32</li>
                    <li>$0.99</li>
                    <li>$1.50</li>
                    <li>$3.97</li>
                    <li>$4.84</li>
                    <li>$5.15</li>
                    <li>$0.99</li>
                    <li>$7.03</li>
                    <li>$3.27</li>
                    <li>$2.99</li>
                    <li>$2.49</li>
                </ul>

                <h2>Total Purchase:</h2>
                <p class="text-xl">$39.20</p>

                <h2>Discounts/Loyalty:</h2>
                <p class="text-xl">-$15.00</p>

                <h2>Amount Paid:</h2>
                <p class="text-xl">-$24.20 (Cash)</p>

                <h2>Change Received:</h2>
                <p class="text-xl">$25.80</p>
              </Message>
            </div>
          </TabPanel>
        </TabView>
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
