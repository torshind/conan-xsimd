from conans import ConanFile, CMake


class XsimdConan(ConanFile):
    name = "xsimd"
    version = "7.2.3"
    license = "BSD 3-Clause"
    homepage = "https://github.com/QuantStack/xtl/"
    url = "https://github.com/torshind/conan-xsimd/"
    description = "Modern, portable C++ wrappers for SIMD intrinsics and parallelized, optimized math implementations" \
                  "(SSE, AVX, NEON, AVX512)"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"
    exports_sources = "*"

    def source(self):
        self.run("git clone --branch "
                 + self.version
                 + " https://github.com/QuantStack/xsimd.git")

    def build(self):
        pass

    def package(self):
        cmake = CMake(self)
        cmake.configure(source_folder="xsimd")
        cmake.install()

    def package_info(self):
        self.info.header_only()
