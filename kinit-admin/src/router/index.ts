import { createRouter, createWebHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'
import type { App } from 'vue'
import { Layout } from '@/utils/routerHelper'
import { useI18n } from '@/hooks/web/useI18n'

const { t } = useI18n()

export const constantRouterMap: AppRouteRecordRaw[] = [
  {
    path: '/',
    component: Layout,
    redirect: '/dashboard/analysis',
    name: 'Root',
    meta: {
      hidden: true
    },
    children: [
      {
        path: 'home',
        name: 'Home',
        component: () => import('@/views/Home/Home.vue'),
        meta: {
          affix: false,
          alwaysShow: true,
          breadcrumb: true,
          canTo: true,
          hidden: true,
          noCache: true,
          noTagsView: false,
          title: '个人主页'
        }
      }
    ]
  },
  {
    path: '/redirect',
    component: Layout,
    name: 'Redirect',
    children: [
      {
        path: '/redirect/:path(.*)',
        name: 'Redirect',
        component: () => import('@/views/Redirect/Redirect.vue'),
        meta: {}
      }
    ],
    meta: {
      hidden: true,
      noTagsView: true
    }
  },
  {
    path: '/login',
    component: () => import('@/views/Login/Login.vue'),
    name: 'Login',
    meta: {
      hidden: true,
      title: t('router.login'),
      noTagsView: true
    }
  },
  {
    path: '/reset/password',
    component: () => import('@/views/Reset/Reset.vue'),
    name: 'ResetPassword',
    meta: {
      hidden: true,
      title: '重置密码',
      noTagsView: true
    }
  },
  {
    path: '/docs',
    name: 'Docs',
    meta: {
      hidden: true,
      title: '在线文档',
      noTagsView: true
    },
    children: [
      {
        path: 'privacy',
        name: 'Privacy',
        component: () => import('@/views/Vadmin/Docs/Privacy.vue'),
        meta: {
          hidden: true,
          title: '隐私政策',
          noTagsView: true
        }
      },
      {
        path: 'agreement',
        name: 'Agreement',
        component: () => import('@/views/Vadmin/Docs/Agreement.vue'),
        meta: {
          hidden: true,
          title: '用户协议',
          noTagsView: true
        }
      }
    ]
  },
  {
    path: '/404',
    component: () => import('@/views/Error/404.vue'),
    name: 'NoFind',
    meta: {
      hidden: true,
      title: '404',
      noTagsView: true
    }
  }
]

export const asyncRouterMap: AppRouteRecordRaw[] = [
  {
    path: '/dashboard',
    component: Layout,
    redirect: '/dashboard/workplace',
    name: 'Dashboard',
    meta: {
      title: t('router.dashboard'),
      icon: 'ant-design:dashboard-filled',
      alwaysShow: true
    },
    children: [
      {
        path: 'workplace',
        component: () => import('@/views/Dashboard/Workplace.vue'),
        name: 'Workplace',
        meta: {
          title: t('router.workplace'),
          noCache: true
        }
      }
    ]
  },
  {
    path: '/video',
    component: Layout,
    name: 'Video',
    meta: {
      title: '第三方稿件管理',
      icon: 'ep:video-play',
      alwaysShow: true
    },
    children: [
      {
        path: 'article',
        component: () => import('@/views/Vadmin/Video/Article.vue'),
        name: 'VideoArticle',
        meta: {
          title: '第三方稿件管理',
          noCache: true
        }
      }
    ]
  },
  {
    path: '/rank',
    component: Layout,
    name: 'Rank',
    meta: {
      title: '排行榜',
      icon: 'ep:trophy',
      alwaysShow: true
    },
    children: [
      {
        path: 'douyin',
        component: () => import('@/views/Vadmin/Rank/DouyinRank.vue'),
        name: 'DouyinRank',
        meta: {
          title: '抖音榜',
          noCache: true
        }
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(),
  strict: true,
  routes: constantRouterMap as RouteRecordRaw[],
  scrollBehavior: () => ({ left: 0, top: 0 })
})

export const resetRouter = (): void => {
  const resetWhiteNameList = [
    'Login',
    'NoFind',
    'Root',
    'ResetPassword',
    'Redirect',
    'Home',
    'Docs',
    'Privacy',
    'Agreement'
  ]
  router.getRoutes().forEach((route) => {
    const { name } = route
    if (name && !resetWhiteNameList.includes(name as string)) {
      router.hasRoute(name) && router.removeRoute(name)
    }
  })
}

// 判断是否已经有某个路径的路由配置
export const hasRoute = (path: string): boolean => {
  const resolvedRoute = router.resolve(path)
  return resolvedRoute.matched.length > 0
}

export const setupRouter = (app: App<Element>) => {
  app.use(router)
}

export default router
