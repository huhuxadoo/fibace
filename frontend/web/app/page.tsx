import { HeroSection } from '@/components/HeroSection'
import { FeaturesGrid } from '@/components/FeaturesGrid'

export default function Home() {
  return (
    <main className="min-h-screen">
      <HeroSection />
      <FeaturesGrid />
    </main>
  )
}
