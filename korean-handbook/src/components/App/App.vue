<template>
  <div id="app" :class="{ home: $route.path === '/' }">
    <div id="nav">
      <div class="nav-content">
        <div style="display: flex; align-items: center;">
          <div class="nav-logo">
            <router-link to="/" class="button--logo">
              <svg
                xmlns:dc="http://purl.org/dc/elements/1.1/"
                xmlns:cc="http://creativecommons.org/ns#"
                xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                xmlns:svg="http://www.w3.org/2000/svg"
                xmlns="http://www.w3.org/2000/svg"
                id="svg8"
                version="1.1"
                viewBox="0 0 100 100"
                height="100mm"
                width="100mm"
                class="logo"
              >
                <defs id="defs2" />
                <metadata id="metadata5" />
                <g
                  transform="translate(0,-100)"
                  id="layer3"
                  style="display: inline;"
                >
                  <g
                    transform="matrix(1.6607495,0,0,1.6607495,-27.391721,-97.587624)"
                    id="g5688"
                    class="shape"
                  >
                    <path
                      d="M 20.708554,126.46606 H 46.20405 l -13.682253,22.73177 13.511422,22.5 -25.324665,-0.009 c 0,0 0.177679,-15.29921 0.180076,-22.52289 0.0026,-7.85095 -0.180076,-22.70005 -0.180076,-22.70005 z"
                      id="path5657"
                      class="shape"
                      style="fill: rgb(254, 254, 254); fill-opacity: 1; stroke: none; stroke-width: 0.0910492px; stroke-linecap: butt; stroke-linejoin: miter; stroke-opacity: 1;"
                    />
                    <circle
                      id="path5661"
                      cx="59.799267"
                      cy="159.10349"
                      r="12.594335"
                      class="shape"
                      style="fill: rgb(254, 254, 254); fill-opacity: 1; stroke: none; stroke-width: 6.97366; stroke-linecap: round; stroke-miterlimit: 4; stroke-dasharray: none; stroke-opacity: 1;"
                    />
                    <g
                      transform="matrix(1.1210374,0,0,1.1210374,-6.8195464,-20.781859)"
                      id="g5704"
                      class="shape"
                    >
                      <rect
                        y="140.33861"
                        x="48.199764"
                        height="4.6655374"
                        width="22.403643"
                        id="rect5665"
                        class="shape"
                        style="fill: rgb(254, 254, 254); fill-opacity: 1; stroke: none; stroke-width: 7.46241; stroke-linecap: round; stroke-miterlimit: 4; stroke-dasharray: none; stroke-opacity: 1;"
                      />
                      <rect
                        y="131.27011"
                        x="57.089748"
                        height="9.3310747"
                        width="4.6655374"
                        id="rect5665-5"
                        class="shape"
                        style="display: inline; fill: rgb(254, 254, 254); fill-opacity: 1; stroke: none; stroke-width: 4.81599; stroke-linecap: round; stroke-miterlimit: 4; stroke-dasharray: none; stroke-opacity: 1;"
                      />
                    </g>
                  </g>
                </g>
                <g transform="translate(0,-100)" id="layer1" />
              </svg>
            </router-link>
          </div>
          <router-link to="/" v-if="windowWidth > 900" class="title">The Korean Handbook</router-link>
        </div>
        <template v-if="$store.state.mobile">
          <div class="nav-links--mobile">
            <button @click="toggleMobileMenu">
              <i class="material-icons">menu</i>
            </button>
          </div>
        </template>
        <template v-else>
          <div class="nav-links">
            <router-link to="/">Home</router-link>
            <router-link to="/random-words/all">Random Words</router-link>
            <router-link to="/info/">Words</router-link>
          </div>
          <div></div>
        </template>
      </div>
    </div>
    <div v-if="$store.state.mobileMenu" class="mobile-menu">
      <div class="mobile-menu-content">
        <div class="nav-links">
          <router-link to="/">Home</router-link>
          <router-link to="/random-words/all">Random Words</router-link>
          <router-link to="/info/">Words</router-link>
        </div>
      </div>
    </div>
    <router-view :mobile="$store.state.mobile" />
  </div>
</template>

<script src="./App.js"></script>

<style lang="scss">
@import './App.scss';
</style>
