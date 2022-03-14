export default {
  namespaced: true,
  state: {
    menuCollapse: false,
  },
  mutations: {
    triggerMenuCollapse(state) {
      state.menuCollapse = !state.menuCollapse;
    },
  },
};
