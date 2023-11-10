<script setup lang="ts">
import { ref } from "vue";

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
        <div class="mt-2">
          <TabView>
            <TabPanel header="Savings AI Bot"> Hello World </TabPanel>
            <TabPanel header="Analysis">
              <p class="m-0">
                Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae
                ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit
                aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Consectetur, adipisci
                velit, sed quia non numquam eius modi.
              </p>
            </TabPanel>
            <TabPanel header="History">
              <p class="m-0">
                At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores
                et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id
                est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est
                eligendi optio cumque nihil impedit quo minus.
              </p>
            </TabPanel>
          </TabView>
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
</style>
