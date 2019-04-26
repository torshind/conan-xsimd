from conans import ConanFile, CMake, tools


class XsimdConan(ConanFile):
    name = "xsimd"
    version = "7.1.3"
    license = "BSD 3-Clause"
    url = "https://github.com/QuantStack/xtl"
    description = "Modern, portable C++ wrappers for SIMD intrinsics and parallelized, optimized math implementations" \
                  "(SSE, AVX, NEON, AVX512)"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"
    exports_sources = "*"

    def source(self):
        git = tools.Git()
        git.clone("https://github.com/QuantStack/xsimd.git", self.version)

    def build(self):
        pass

    def package(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.install()

    def package_info(self):
        self.info.header_only()
        self.cpp_info.libs = ["xsimd"]
