/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, {
/******/ 				configurable: false,
/******/ 				enumerable: true,
/******/ 				get: getter
/******/ 			});
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = "./templates/insurance/risks/risks.js");
/******/ })
/************************************************************************/
/******/ ({

/***/ "./templates/insurance/risks/risks.js":
/*!********************************************!*\
  !*** ./templates/insurance/risks/risks.js ***!
  \********************************************/
/*! no static exports found */
/***/ (function(module, exports) {

eval("// Vue.component('todo-item', {\n//   // The todo-item component now accepts a\n//   // \"prop\", which is like a custom attribute.\n//   // This prop is called todo.\n//   props: ['todo'],\n//   template: '<li>{{ todo.text }}</li>'\n// });\n\n// import Vue from 'vue';\n// import VueMonthlyPicker from 'vue-monthly-picker';\n\n// Vue.component('date-field', {\n//     components: {\n//         'vue-monthly-picker'\n//     }\n// });\n\nVue.component('text-field', {\n  template: '<textarea></textarea>'\n});\n\nnew Vue({\n    delimiters: ['[[', ']]'],\n    el: '#risks-app',\n    data: {\n      risks: ['r1', 'r2', 'r2']\n    }\n});\n\n\n//# sourceURL=webpack:///./templates/insurance/risks/risks.js?");

/***/ })

/******/ });