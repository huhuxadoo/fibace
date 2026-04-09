export function HeroSection() {
  return (
    <section className="relative py-20 px-4 sm:px-6 lg:px-8 overflow-hidden">
      <div className="absolute inset-0 bg-gradient-to-br from-primary-900/20 to-purple-900/20" />
      <div className="relative max-w-7xl mx-auto text-center">
        <h1 className="text-5xl sm:text-6xl font-bold mb-6 bg-gradient-to-r from-white to-gray-400 bg-clip-text text-transparent">
          FiBace
        </h1>
        <p className="text-xl sm:text-2xl text-gray-400 mb-8 max-w-2xl mx-auto">
          Умное управление арендной недвижимостью. Автоматизация для арендодателей и арендаторов.
        </p>
        <div className="flex flex-col sm:flex-row gap-4 justify-center">
          <button className="btn-primary">
            Начать бесплатно
          </button>
          <button className="px-6 py-3 border border-white/20 hover:bg-white/5 rounded-lg transition-all">
            Узнать больше
          </button>
        </div>
      </div>
    </section>
  )
}
