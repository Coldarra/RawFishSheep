<template>
  <div id="bs-dashboard">
    <div class="bs-title">
      <div class="bs-title-text">
        仪表盘
        <div class="pull-right">
          <template>
            <el-select v-model="dashboard_date_value" placeholder="请选择">
              <el-option
                v-for="(item,id) in dashboard_date_options"
                :key="id.value"
                :label="item.label"
                :value="item.value"
              ></el-option>
            </el-select>
          </template>
        </div>
      </div>
    </div>

    <el-row :gutter="20" id="bs-dashboard-head">
      <el-col :span="6">
        <el-card class="box-card bs-item">
          <div class="item-title">销售数量</div>
          <div class="item-text">52</div>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card class="box-card bs-item">
          <div class="item-title">订单数量</div>
          <div class="item-text">27</div>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card class="box-card bs-item">
          <div class="item-title">成交金额</div>
          <div class="item-text">¥ 328.00</div>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card class="box-card bs-item">
          <div class="item-title">成交金额</div>
          <div class="item-text">¥ 328.00</div>
        </el-card>
      </el-col>
    </el-row>
    <br>
    <el-row :gutter="20">
      <el-col :span="0">
        <div class="chart-area" id="chart_example1" style="height:30rem"></div>
      </el-col>
      <el-col :span="16">
        <div class="chart-area" id="chart_example3" style="height:30rem"></div>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="16">
        <div class="chart-area" id="chart_example2" style="height:30rem"></div>
      </el-col>
    </el-row>
  </div>
</template>
<style lang="scss" scoped>
</style>

<style lang="scss" >
#bs-dashboard {
  #bs-dashboard-head {
    margin-bottom: 1rem;
  }
}
.bs-title {
  margin-left: 0.5rem;
  margin-right: 0.5rem;
  margin-top: 0.5rem;
  margin-bottom: 1rem;
  .bs-title-text {
    font-size: 1.7rem;
  }
}
.bs-item {
  .item-title {
    margin-bottom: 0.5rem;
    color: #a6b9c5;
  }
  .item-text {
    font-size: 1.3rem;
  }
}
.chart-area {
  margin-left: 0.5rem;
  margin-right: 0.5rem;
  margin-top: 0.5rem;
  margin-bottom: 0.5rem;
  background-color: white;
}
</style>


<script>
import echarts from "echarts";

export default {
  name: "bs-dashboard",

  data() {
    return {
      dashboard_date_value: "today",
      dashboard_date_options: [
        {
          value: "today",
          label: "当日"
        },
        {
          value: "3days",
          label: "最近三天"
        },
        {
          value: "week",
          label: "最近一周"
        },
        {
          value: "month",
          label: "最近一月"
        }
      ]
    };
  },
  mounted() {
    let myChart1 = echarts.init(document.getElementById("chart_example1"));
    let myChart2 = echarts.init(document.getElementById("chart_example2"));
    let myChart3 = echarts.init(document.getElementById("chart_example3"));
    let option1 = {
      title: {
        left: "center",
        text: "月销量统计图"
      },
      color: ["#f44"],
      tooltip: {
        trigger: "axis",
        axisPointer: {
          type: "shadow"
        }
      },
      xAxis: [
        {
          type: "category",
          data: ["1月", "2月", "3月", "4月", "5月"],
          axisTick: {
            alignWithLabel: true
          }
        }
      ],
      yAxis: [
        {
          type: "value"
        }
      ],
      series: [
        {
          name: "当月销售额",
          type: "bar",
          barWidth: "60%",
          data: [995, 666, 444, 858, 654]
        }
      ]
    };
    let option2 = {
      tooltip: {
        trigger: "axis",
        axisPointer: {
          // 坐标轴指示器，坐标轴触发有效
          type: "shadow" // 默认为直线，可选为：'line' | 'shadow'
        }
      },
      title: {
        left: "left",
        text: "分类销量统计图"
      },
      legend: {
        data: ["蔬菜", "水果", "海鲜", "肉类", "其他"]
      },
      grid: {
        left: "3%",
        right: "4%",
        bottom: "3%",
        containLabel: true
      },
      xAxis: {
        type: "value"
      },
      yAxis: {
        type: "category",
        data: ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
      },
      series: [
        {
          name: "蔬菜",
          type: "bar",
          stack: "总量",
          label: {
            normal: {
              show: true,
              position: "insideRight"
            }
          },
          data: [320, 302, 301, 334, 390, 330, 320]
        },
        {
          name: "水果",
          type: "bar",
          stack: "总量",
          label: {
            normal: {
              show: true,
              position: "insideRight"
            }
          },
          data: [120, 132, 101, 134, 90, 230, 210]
        },
        {
          name: "海鲜",
          type: "bar",
          stack: "总量",
          label: {
            normal: {
              show: true,
              position: "insideRight"
            }
          },
          data: [220, 182, 191, 234, 290, 330, 310]
        },
        {
          name: "肉类",
          type: "bar",
          stack: "总量",
          label: {
            normal: {
              show: true,
              position: "insideRight"
            }
          },
          data: [150, 212, 201, 154, 190, 330, 410]
        },
        {
          name: "其他",
          type: "bar",
          stack: "总量",
          label: {
            normal: {
              show: true,
              position: "insideRight"
            }
          },
          data: [820, 832, 901, 934, 1290, 1330, 1320]
        }
      ]
    };
    let colors = ["#5793f3", "#d14a61", "#675bba"];
    let option3 = {
      color: colors,

      tooltip: {
        trigger: "axis",
        axisPointer: {
          type: "cross"
        }
      },
      grid: {
        right: "20%"
      },
      toolbox: {
        feature: {
          dataView: { show: true, readOnly: false },
          restore: { show: true },
          saveAsImage: { show: true }
        }
      },
      legend: {
        data: ["月活跃用户", "月订单量", "月销售额"]
      },
      xAxis: [
        {
          type: "category",
          axisTick: {
            alignWithLabel: true
          },
          data: [
            "12月",
            "1月",
            "2月",
            "3月",
            "4月",
          ]
        }
      ],
      yAxis: [
        {
          type: "value",
          name: "月活跃用户",
          min: 0,
          max: 250,
          position: "right",
          axisLine: {
            lineStyle: {
              color: colors[0]
            }
          },
          axisLabel: {
            formatter: "{value} 人"
          }
        },
        {
          type: "value",
          name: "月订单量",
          min: 0,
          max: 500,
          position: "right",
          offset: 80,
          axisLine: {
            lineStyle: {
              color: colors[1]
            }
          },
          axisLabel: {
            formatter: "{value} 单"
          }
        },
        {
          type: "value",
          name: "月销售额",
          min: 0,
          max: 10000,
          position: "left",
          axisLine: {
            lineStyle: {
              color: colors[2]
            }
          },
          axisLabel: {
            formatter: "{value} 元"
          }
        }
      ],
      series: [
        {
          name: "月活跃用户",
          type: "bar",
          data: [
            23,
            34,
            76,
            136,
            162,
          ]
        },
        {
          name: "月订单量",
          type: "bar",
          yAxisIndex: 1,
          data: [
            46,
            73,
            170,
            276,
            482,
          ]
        },
        {
          name: "月销售额",
          type: "line",
          yAxisIndex: 2,
          data: [
            802,
            1463,
            3306,
            5840,
            9012,
          ]
        }
      ]
    };

    myChart1.setOption(option1);
    myChart2.setOption(option2);
    myChart3.setOption(option3);

    window.addEventListener("resize", function() {
      myChart.resize();
    });
  },
  methods: {},
  watch: {},
  created() {}
};
</script>
