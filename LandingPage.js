import React from 'react';
import { Button } from '@/components/ui/button';
import { motion } from 'framer-motion';
import { Github, BookOpen, LayoutDashboard, Terminal, Zap } from 'lucide-react';

const LandingPage = () => {
  return (
    <div className="min-h-screen bg-black text-white flex flex-col">
      {/* Hero Section */}
      <header className="flex-grow flex items-center justify-center p-4">
        <div className="text-center space-y-6">
          <motion.h1
            initial={{ opacity: 0, y: -50 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, ease: 'easeInOut' }}
            className="text-4xl sm:text-5xl md:text-6xl lg:text-7xl font-extrabold bg-clip-text text-transparent bg-gradient-to-r from-purple-400 to-pink-600"
          >
            Your AI-Powered Assistant
          </motion.h1>
          <motion.p
            initial={{ opacity: 0, y: 50 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, ease: 'easeInOut', delay: 0.2 }}
            className="text-lg sm:text-xl md:text-2xl text-gray-300 max-w-3xl mx-auto"
          >
            Supercharge your workflow with AI.  Interact with documents,
            understand code, generate content, and more.
          </motion.p>
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 0.8, ease: 'easeInOut', delay: 0.4 }}
            className="flex flex-col sm:flex-row justify-center gap-4"
          >
            <Button
              variant="default"
              size="lg"
              className="bg-gradient-to-r from-purple-500 to-pink-500 text-white hover:from-purple-600 hover:to-pink-600
                         px-6 py-3 rounded-full shadow-lg hover:shadow-xl transition-all duration-300
                         font-semibold text-lg flex items-center gap-2"
            >
              <Zap className="w-5 h-5" /> Get Started
            </Button>
            <Button
              variant="outline"
              size="lg"
              className="text-white hover:bg-white/10 border-gray-700 hover:border-gray-600
                         px-6 py-3 rounded-full transition-colors duration-300
                         font-semibold text-lg flex items-center gap-2"
            >
              <Github className="w-5 h-5" />
              GitHub
            </Button>
          </motion.div>
        </div>
      </header>

      {/* Features Section */}
      <section className="py-16 px-4 sm:px-6 lg:px-8">
        <div className="max-w-7xl mx-auto space-y-12">
          <h2 className="text-3xl sm:text-4xl font-semibold text-center text-gray-200">
            Key Features
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10">
            <FeatureCard
              title="Document Interaction"
              description="Upload and analyze documents.  Ask questions, summarize content, and extract key information."
              icon={<BookOpen className="w-8 h-8 text-purple-400 mb-4" />}
            />
            <FeatureCard
              title="Code Understanding"
              description="Analyze and understand code snippets.  Explain functionality, identify issues, and generate documentation."
              icon={<Terminal className="w-8 h-8 text-blue-400 mb-4" />}
            />
            <FeatureCard
              title="Content Generation"
              description="Generate various content formats, including articles, summaries, and creative text."
              icon={<LayoutDashboard className="w-8 h-8 text-green-400 mb-4" />}
            />
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="py-8 px-4 sm:px-6 lg:px-8 text-center text-gray-400 border-t border-gray-800">
        <p>© {new Date().getFullYear()} My AI Assistant. All rights reserved.</p>
      </footer>
    </div>
  );
};

const FeatureCard = ({ title, description, icon }) => { // Removed TypeScript type annotations
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      whileInView={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.6 }}
      viewport={{ once: true }}
      className="bg-gray-900 rounded-xl p-6 shadow-lg border border-gray-800 hover:border-gray-700 transition-all duration-300 hover:shadow-xl"
    >
      {icon}
      <h3 className="text-xl font-semibold text-white mb-2">{title}</h3>
      <p className="text-gray-300">{description}</p>
    </motion.div>
  );
};

export default LandingPage;
