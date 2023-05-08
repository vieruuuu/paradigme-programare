import org.jetbrains.kotlin.gradle.*

plugins {
  kotlin("jvm") version "1.8.21" // Kotlin version to use
  application // Application plugin. Also see 1️⃣ below the code
}

group = "org.example" // A company name, for example, `org.jetbrains`

version = "1.0-SNAPSHOT" // Version to assign to the built artifact

repositories { mavenCentral() }

dependencies { // All the libraries you want to use. See 4️⃣
  // Copy dependencies' names after you find them in a repository
  testImplementation(kotlin("test")) // The Kotlin test library
  implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.7.0-RC")
  implementation("org.jetbrains.kotlinx:kotlinx-coroutines-debug:1.7.0-RC")
}

tasks.test { // See 5️⃣
  useJUnitPlatform() // JUnitPlatform for tests. See 6️⃣
}

// tasks.named("compileKotlin", org.jetbrains.kotlin.gradle.tasks.KotlinCompilationTask::class.java)
// {
//   compilerOptions {
//     freeCompilerArgs.addAll(
//         listOf(
//             "-Xuse-experimental=kotlinx.coroutines.ExperimentalCoroutinesApi",
//             "-Xuse-experimental=kotlinx.coroutines.ExperimentalCoroutinesApi"
//         )
//     )
//   }
// }

kotlin { // Extension for easy setup
  jvmToolchain(8) // Target version of generated JVM bytecode. See 7️⃣
}

application {
  mainClass.set("MainKt") // The main class of the application
}
