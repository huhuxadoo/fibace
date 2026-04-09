const features = [
  { title: 'Автоматизация', desc: 'Умные контракты и напоминания', icon: '⚡' },
  { title: 'Аналитика', desc: 'Доходы и расходы в реальном времени', icon: '📊' },
  { title: 'Безопасность', desc: 'Верификация и страхование', icon: '🛡️' },
]

export function FeaturesGrid() {
  return (
    <section className="py-20 px-4 sm:px-6 lg:px-8">
      <div className="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-8">
        {features.map((feature) => (
          <div key={feature.title} className="glass-panel p-8 hover:bg-white/10 transition-all">
            <div className="text-4xl mb-4">{feature.icon}</div>
            <h3 className="text-xl font-semibold mb-2">{feature.title}</h3>
            <p className="text-gray-400">{feature.desc}</p>
          </div>
        ))}
      </div>
    </section>
  )
}
