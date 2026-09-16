from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_apps_install_create_active_error_component import (
        ApiV1KubernetesAppsInstallCreateActiveErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_actual_availability_error_component import (
        ApiV1KubernetesAppsInstallCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_annotations_error_component import (
        ApiV1KubernetesAppsInstallCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_archived_at_error_component import (
        ApiV1KubernetesAppsInstallCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_archived_by_error_component import (
        ApiV1KubernetesAppsInstallCreateArchivedByErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_archived_error_component import (
        ApiV1KubernetesAppsInstallCreateArchivedErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_archived_reason_error_component import (
        ApiV1KubernetesAppsInstallCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_artifact_error_component import (
        ApiV1KubernetesAppsInstallCreateArtifactErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_artifact_package_error_component import (
        ApiV1KubernetesAppsInstallCreateArtifactPackageErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_block_error_component import (
        ApiV1KubernetesAppsInstallCreateBlockErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_byoa_error_component import (
        ApiV1KubernetesAppsInstallCreateByoaErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_catalogue_app_error_component import (
        ApiV1KubernetesAppsInstallCreateCatalogueAppErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_created_by_component_error_component import (
        ApiV1KubernetesAppsInstallCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_created_by_user_error_component import (
        ApiV1KubernetesAppsInstallCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_criticality_error_component import (
        ApiV1KubernetesAppsInstallCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_debug_mode_error_component import (
        ApiV1KubernetesAppsInstallCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_description_error_component import (
        ApiV1KubernetesAppsInstallCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_discovery_enabled_error_component import (
        ApiV1KubernetesAppsInstallCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_display_name_error_component import (
        ApiV1KubernetesAppsInstallCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_excluded_from_downtime_until_error_component import (
        ApiV1KubernetesAppsInstallCreateExcludedFromDowntimeUntilErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_ha_enabled_error_component import (
        ApiV1KubernetesAppsInstallCreateHaEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_helm_chart_error_component import (
        ApiV1KubernetesAppsInstallCreateHelmChartErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_installation_failed_error_component import (
        ApiV1KubernetesAppsInstallCreateInstallationFailedErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_installation_running_error_component import (
        ApiV1KubernetesAppsInstallCreateInstallationRunningErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_installed_error_component import (
        ApiV1KubernetesAppsInstallCreateInstalledErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_installed_version_error_component import (
        ApiV1KubernetesAppsInstallCreateInstalledVersionErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_k8s_cluster_error_component import (
        ApiV1KubernetesAppsInstallCreateK8SClusterErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_kind_error_component import (
        ApiV1KubernetesAppsInstallCreateKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_labels_error_component import (
        ApiV1KubernetesAppsInstallCreateLabelsErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_last_installation_error_component import (
        ApiV1KubernetesAppsInstallCreateLastInstallationErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_last_metrics_check_error_component import (
        ApiV1KubernetesAppsInstallCreateLastMetricsCheckErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1KubernetesAppsInstallCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_managed_by_content_type_error_component import (
        ApiV1KubernetesAppsInstallCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_managed_by_object_id_error_component import (
        ApiV1KubernetesAppsInstallCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_modified_by_user_error_component import (
        ApiV1KubernetesAppsInstallCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_name_error_component import (
        ApiV1KubernetesAppsInstallCreateNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_namespace_error_component import (
        ApiV1KubernetesAppsInstallCreateNamespaceErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_non_field_errors_error_component import (
        ApiV1KubernetesAppsInstallCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_platform_dns_record_created_error_component import (
        ApiV1KubernetesAppsInstallCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_platform_service_error_component import (
        ApiV1KubernetesAppsInstallCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_pods_available_error_component import (
        ApiV1KubernetesAppsInstallCreatePodsAvailableErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_pods_details_error_component import (
        ApiV1KubernetesAppsInstallCreatePodsDetailsErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_pods_ready_error_component import (
        ApiV1KubernetesAppsInstallCreatePodsReadyErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_pods_restart_count_last_hour_error_component import (
        ApiV1KubernetesAppsInstallCreatePodsRestartCountLastHourErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_pods_restart_count_total_error_component import (
        ApiV1KubernetesAppsInstallCreatePodsRestartCountTotalErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_pods_status_hash_error_component import (
        ApiV1KubernetesAppsInstallCreatePodsStatusHashErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_pods_status_updated_at_error_component import (
        ApiV1KubernetesAppsInstallCreatePodsStatusUpdatedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_pods_total_error_component import (
        ApiV1KubernetesAppsInstallCreatePodsTotalErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_pods_unavailable_error_component import (
        ApiV1KubernetesAppsInstallCreatePodsUnavailableErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_provider_error_component import (
        ApiV1KubernetesAppsInstallCreateProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_provider_id_error_component import (
        ApiV1KubernetesAppsInstallCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_provider_reference_error_component import (
        ApiV1KubernetesAppsInstallCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_reconciliation_enabled_error_component import (
        ApiV1KubernetesAppsInstallCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_scope_error_component import (
        ApiV1KubernetesAppsInstallCreateScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_sla_availability_error_component import (
        ApiV1KubernetesAppsInstallCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_sla_target_error_component import (
        ApiV1KubernetesAppsInstallCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_sla_window_days_error_component import (
        ApiV1KubernetesAppsInstallCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_slo_availability_error_component import (
        ApiV1KubernetesAppsInstallCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_slo_target_error_component import (
        ApiV1KubernetesAppsInstallCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_slo_window_days_error_component import (
        ApiV1KubernetesAppsInstallCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_source_error_component import (
        ApiV1KubernetesAppsInstallCreateSourceErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_target_availability_error_component import (
        ApiV1KubernetesAppsInstallCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_uninstallation_failed_error_component import (
        ApiV1KubernetesAppsInstallCreateUninstallationFailedErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_uninstallation_running_error_component import (
        ApiV1KubernetesAppsInstallCreateUninstallationRunningErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_install_create_uninstalled_error_component import (
        ApiV1KubernetesAppsInstallCreateUninstalledErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesAppsInstallCreateValidationError")


@_attrs_define
class ApiV1KubernetesAppsInstallCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesAppsInstallCreateActiveErrorComponent |
            ApiV1KubernetesAppsInstallCreateActualAvailabilityErrorComponent |
            ApiV1KubernetesAppsInstallCreateAnnotationsErrorComponent |
            ApiV1KubernetesAppsInstallCreateArchivedAtErrorComponent |
            ApiV1KubernetesAppsInstallCreateArchivedByErrorComponent |
            ApiV1KubernetesAppsInstallCreateArchivedErrorComponent |
            ApiV1KubernetesAppsInstallCreateArchivedReasonErrorComponent |
            ApiV1KubernetesAppsInstallCreateArtifactErrorComponent |
            ApiV1KubernetesAppsInstallCreateArtifactPackageErrorComponent |
            ApiV1KubernetesAppsInstallCreateBlockErrorComponent | ApiV1KubernetesAppsInstallCreateByoaErrorComponent |
            ApiV1KubernetesAppsInstallCreateCatalogueAppErrorComponent |
            ApiV1KubernetesAppsInstallCreateCreatedByComponentErrorComponent |
            ApiV1KubernetesAppsInstallCreateCreatedByUserErrorComponent |
            ApiV1KubernetesAppsInstallCreateCriticalityErrorComponent |
            ApiV1KubernetesAppsInstallCreateDebugModeErrorComponent |
            ApiV1KubernetesAppsInstallCreateDescriptionErrorComponent |
            ApiV1KubernetesAppsInstallCreateDiscoveryEnabledErrorComponent |
            ApiV1KubernetesAppsInstallCreateDisplayNameErrorComponent |
            ApiV1KubernetesAppsInstallCreateExcludedFromDowntimeUntilErrorComponent |
            ApiV1KubernetesAppsInstallCreateHaEnabledErrorComponent |
            ApiV1KubernetesAppsInstallCreateHelmChartErrorComponent |
            ApiV1KubernetesAppsInstallCreateInstallationFailedErrorComponent |
            ApiV1KubernetesAppsInstallCreateInstallationRunningErrorComponent |
            ApiV1KubernetesAppsInstallCreateInstalledErrorComponent |
            ApiV1KubernetesAppsInstallCreateInstalledVersionErrorComponent |
            ApiV1KubernetesAppsInstallCreateK8SClusterErrorComponent | ApiV1KubernetesAppsInstallCreateKindErrorComponent |
            ApiV1KubernetesAppsInstallCreateLabelsErrorComponent |
            ApiV1KubernetesAppsInstallCreateLastInstallationErrorComponent |
            ApiV1KubernetesAppsInstallCreateLastMetricsCheckErrorComponent |
            ApiV1KubernetesAppsInstallCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1KubernetesAppsInstallCreateManagedByContentTypeErrorComponent |
            ApiV1KubernetesAppsInstallCreateManagedByObjectIdErrorComponent |
            ApiV1KubernetesAppsInstallCreateModifiedByUserErrorComponent |
            ApiV1KubernetesAppsInstallCreateNameErrorComponent | ApiV1KubernetesAppsInstallCreateNamespaceErrorComponent |
            ApiV1KubernetesAppsInstallCreateNonFieldErrorsErrorComponent |
            ApiV1KubernetesAppsInstallCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1KubernetesAppsInstallCreatePlatformServiceErrorComponent |
            ApiV1KubernetesAppsInstallCreatePodsAvailableErrorComponent |
            ApiV1KubernetesAppsInstallCreatePodsDetailsErrorComponent |
            ApiV1KubernetesAppsInstallCreatePodsReadyErrorComponent |
            ApiV1KubernetesAppsInstallCreatePodsRestartCountLastHourErrorComponent |
            ApiV1KubernetesAppsInstallCreatePodsRestartCountTotalErrorComponent |
            ApiV1KubernetesAppsInstallCreatePodsStatusHashErrorComponent |
            ApiV1KubernetesAppsInstallCreatePodsStatusUpdatedAtErrorComponent |
            ApiV1KubernetesAppsInstallCreatePodsTotalErrorComponent |
            ApiV1KubernetesAppsInstallCreatePodsUnavailableErrorComponent |
            ApiV1KubernetesAppsInstallCreateProviderErrorComponent |
            ApiV1KubernetesAppsInstallCreateProviderIdErrorComponent |
            ApiV1KubernetesAppsInstallCreateProviderReferenceErrorComponent |
            ApiV1KubernetesAppsInstallCreateReconciliationEnabledErrorComponent |
            ApiV1KubernetesAppsInstallCreateScopeErrorComponent |
            ApiV1KubernetesAppsInstallCreateSlaAvailabilityErrorComponent |
            ApiV1KubernetesAppsInstallCreateSlaTargetErrorComponent |
            ApiV1KubernetesAppsInstallCreateSlaWindowDaysErrorComponent |
            ApiV1KubernetesAppsInstallCreateSloAvailabilityErrorComponent |
            ApiV1KubernetesAppsInstallCreateSloTargetErrorComponent |
            ApiV1KubernetesAppsInstallCreateSloWindowDaysErrorComponent |
            ApiV1KubernetesAppsInstallCreateSourceErrorComponent |
            ApiV1KubernetesAppsInstallCreateTargetAvailabilityErrorComponent |
            ApiV1KubernetesAppsInstallCreateUninstallationFailedErrorComponent |
            ApiV1KubernetesAppsInstallCreateUninstallationRunningErrorComponent |
            ApiV1KubernetesAppsInstallCreateUninstalledErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesAppsInstallCreateActiveErrorComponent
        | ApiV1KubernetesAppsInstallCreateActualAvailabilityErrorComponent
        | ApiV1KubernetesAppsInstallCreateAnnotationsErrorComponent
        | ApiV1KubernetesAppsInstallCreateArchivedAtErrorComponent
        | ApiV1KubernetesAppsInstallCreateArchivedByErrorComponent
        | ApiV1KubernetesAppsInstallCreateArchivedErrorComponent
        | ApiV1KubernetesAppsInstallCreateArchivedReasonErrorComponent
        | ApiV1KubernetesAppsInstallCreateArtifactErrorComponent
        | ApiV1KubernetesAppsInstallCreateArtifactPackageErrorComponent
        | ApiV1KubernetesAppsInstallCreateBlockErrorComponent
        | ApiV1KubernetesAppsInstallCreateByoaErrorComponent
        | ApiV1KubernetesAppsInstallCreateCatalogueAppErrorComponent
        | ApiV1KubernetesAppsInstallCreateCreatedByComponentErrorComponent
        | ApiV1KubernetesAppsInstallCreateCreatedByUserErrorComponent
        | ApiV1KubernetesAppsInstallCreateCriticalityErrorComponent
        | ApiV1KubernetesAppsInstallCreateDebugModeErrorComponent
        | ApiV1KubernetesAppsInstallCreateDescriptionErrorComponent
        | ApiV1KubernetesAppsInstallCreateDiscoveryEnabledErrorComponent
        | ApiV1KubernetesAppsInstallCreateDisplayNameErrorComponent
        | ApiV1KubernetesAppsInstallCreateExcludedFromDowntimeUntilErrorComponent
        | ApiV1KubernetesAppsInstallCreateHaEnabledErrorComponent
        | ApiV1KubernetesAppsInstallCreateHelmChartErrorComponent
        | ApiV1KubernetesAppsInstallCreateInstallationFailedErrorComponent
        | ApiV1KubernetesAppsInstallCreateInstallationRunningErrorComponent
        | ApiV1KubernetesAppsInstallCreateInstalledErrorComponent
        | ApiV1KubernetesAppsInstallCreateInstalledVersionErrorComponent
        | ApiV1KubernetesAppsInstallCreateK8SClusterErrorComponent
        | ApiV1KubernetesAppsInstallCreateKindErrorComponent
        | ApiV1KubernetesAppsInstallCreateLabelsErrorComponent
        | ApiV1KubernetesAppsInstallCreateLastInstallationErrorComponent
        | ApiV1KubernetesAppsInstallCreateLastMetricsCheckErrorComponent
        | ApiV1KubernetesAppsInstallCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1KubernetesAppsInstallCreateManagedByContentTypeErrorComponent
        | ApiV1KubernetesAppsInstallCreateManagedByObjectIdErrorComponent
        | ApiV1KubernetesAppsInstallCreateModifiedByUserErrorComponent
        | ApiV1KubernetesAppsInstallCreateNameErrorComponent
        | ApiV1KubernetesAppsInstallCreateNamespaceErrorComponent
        | ApiV1KubernetesAppsInstallCreateNonFieldErrorsErrorComponent
        | ApiV1KubernetesAppsInstallCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1KubernetesAppsInstallCreatePlatformServiceErrorComponent
        | ApiV1KubernetesAppsInstallCreatePodsAvailableErrorComponent
        | ApiV1KubernetesAppsInstallCreatePodsDetailsErrorComponent
        | ApiV1KubernetesAppsInstallCreatePodsReadyErrorComponent
        | ApiV1KubernetesAppsInstallCreatePodsRestartCountLastHourErrorComponent
        | ApiV1KubernetesAppsInstallCreatePodsRestartCountTotalErrorComponent
        | ApiV1KubernetesAppsInstallCreatePodsStatusHashErrorComponent
        | ApiV1KubernetesAppsInstallCreatePodsStatusUpdatedAtErrorComponent
        | ApiV1KubernetesAppsInstallCreatePodsTotalErrorComponent
        | ApiV1KubernetesAppsInstallCreatePodsUnavailableErrorComponent
        | ApiV1KubernetesAppsInstallCreateProviderErrorComponent
        | ApiV1KubernetesAppsInstallCreateProviderIdErrorComponent
        | ApiV1KubernetesAppsInstallCreateProviderReferenceErrorComponent
        | ApiV1KubernetesAppsInstallCreateReconciliationEnabledErrorComponent
        | ApiV1KubernetesAppsInstallCreateScopeErrorComponent
        | ApiV1KubernetesAppsInstallCreateSlaAvailabilityErrorComponent
        | ApiV1KubernetesAppsInstallCreateSlaTargetErrorComponent
        | ApiV1KubernetesAppsInstallCreateSlaWindowDaysErrorComponent
        | ApiV1KubernetesAppsInstallCreateSloAvailabilityErrorComponent
        | ApiV1KubernetesAppsInstallCreateSloTargetErrorComponent
        | ApiV1KubernetesAppsInstallCreateSloWindowDaysErrorComponent
        | ApiV1KubernetesAppsInstallCreateSourceErrorComponent
        | ApiV1KubernetesAppsInstallCreateTargetAvailabilityErrorComponent
        | ApiV1KubernetesAppsInstallCreateUninstallationFailedErrorComponent
        | ApiV1KubernetesAppsInstallCreateUninstallationRunningErrorComponent
        | ApiV1KubernetesAppsInstallCreateUninstalledErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_apps_install_create_active_error_component import (
            ApiV1KubernetesAppsInstallCreateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_actual_availability_error_component import (
            ApiV1KubernetesAppsInstallCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_annotations_error_component import (
            ApiV1KubernetesAppsInstallCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_archived_at_error_component import (
            ApiV1KubernetesAppsInstallCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_archived_by_error_component import (
            ApiV1KubernetesAppsInstallCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_archived_error_component import (
            ApiV1KubernetesAppsInstallCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_archived_reason_error_component import (
            ApiV1KubernetesAppsInstallCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_artifact_error_component import (
            ApiV1KubernetesAppsInstallCreateArtifactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_artifact_package_error_component import (
            ApiV1KubernetesAppsInstallCreateArtifactPackageErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_block_error_component import (
            ApiV1KubernetesAppsInstallCreateBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_byoa_error_component import (
            ApiV1KubernetesAppsInstallCreateByoaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_catalogue_app_error_component import (
            ApiV1KubernetesAppsInstallCreateCatalogueAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_created_by_component_error_component import (
            ApiV1KubernetesAppsInstallCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_created_by_user_error_component import (
            ApiV1KubernetesAppsInstallCreateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_criticality_error_component import (
            ApiV1KubernetesAppsInstallCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_debug_mode_error_component import (
            ApiV1KubernetesAppsInstallCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_description_error_component import (
            ApiV1KubernetesAppsInstallCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_discovery_enabled_error_component import (
            ApiV1KubernetesAppsInstallCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_display_name_error_component import (
            ApiV1KubernetesAppsInstallCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_excluded_from_downtime_until_error_component import (
            ApiV1KubernetesAppsInstallCreateExcludedFromDowntimeUntilErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_ha_enabled_error_component import (
            ApiV1KubernetesAppsInstallCreateHaEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_helm_chart_error_component import (
            ApiV1KubernetesAppsInstallCreateHelmChartErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_installation_failed_error_component import (
            ApiV1KubernetesAppsInstallCreateInstallationFailedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_installation_running_error_component import (
            ApiV1KubernetesAppsInstallCreateInstallationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_installed_error_component import (
            ApiV1KubernetesAppsInstallCreateInstalledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_installed_version_error_component import (
            ApiV1KubernetesAppsInstallCreateInstalledVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_kind_error_component import (
            ApiV1KubernetesAppsInstallCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_labels_error_component import (
            ApiV1KubernetesAppsInstallCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_last_installation_error_component import (
            ApiV1KubernetesAppsInstallCreateLastInstallationErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_last_metrics_check_error_component import (
            ApiV1KubernetesAppsInstallCreateLastMetricsCheckErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1KubernetesAppsInstallCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_managed_by_content_type_error_component import (
            ApiV1KubernetesAppsInstallCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_managed_by_object_id_error_component import (
            ApiV1KubernetesAppsInstallCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_modified_by_user_error_component import (
            ApiV1KubernetesAppsInstallCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_name_error_component import (
            ApiV1KubernetesAppsInstallCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_namespace_error_component import (
            ApiV1KubernetesAppsInstallCreateNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_non_field_errors_error_component import (
            ApiV1KubernetesAppsInstallCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_platform_dns_record_created_error_component import (
            ApiV1KubernetesAppsInstallCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_platform_service_error_component import (
            ApiV1KubernetesAppsInstallCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_pods_available_error_component import (
            ApiV1KubernetesAppsInstallCreatePodsAvailableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_pods_details_error_component import (
            ApiV1KubernetesAppsInstallCreatePodsDetailsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_pods_ready_error_component import (
            ApiV1KubernetesAppsInstallCreatePodsReadyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_pods_restart_count_last_hour_error_component import (
            ApiV1KubernetesAppsInstallCreatePodsRestartCountLastHourErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_pods_restart_count_total_error_component import (
            ApiV1KubernetesAppsInstallCreatePodsRestartCountTotalErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_pods_status_hash_error_component import (
            ApiV1KubernetesAppsInstallCreatePodsStatusHashErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_pods_status_updated_at_error_component import (
            ApiV1KubernetesAppsInstallCreatePodsStatusUpdatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_pods_total_error_component import (
            ApiV1KubernetesAppsInstallCreatePodsTotalErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_pods_unavailable_error_component import (
            ApiV1KubernetesAppsInstallCreatePodsUnavailableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_provider_error_component import (
            ApiV1KubernetesAppsInstallCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_provider_id_error_component import (
            ApiV1KubernetesAppsInstallCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_provider_reference_error_component import (
            ApiV1KubernetesAppsInstallCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesAppsInstallCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_scope_error_component import (
            ApiV1KubernetesAppsInstallCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_sla_availability_error_component import (
            ApiV1KubernetesAppsInstallCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_sla_target_error_component import (
            ApiV1KubernetesAppsInstallCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_sla_window_days_error_component import (
            ApiV1KubernetesAppsInstallCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_slo_availability_error_component import (
            ApiV1KubernetesAppsInstallCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_slo_target_error_component import (
            ApiV1KubernetesAppsInstallCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_slo_window_days_error_component import (
            ApiV1KubernetesAppsInstallCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_source_error_component import (
            ApiV1KubernetesAppsInstallCreateSourceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_target_availability_error_component import (
            ApiV1KubernetesAppsInstallCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_uninstallation_failed_error_component import (
            ApiV1KubernetesAppsInstallCreateUninstallationFailedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_uninstallation_running_error_component import (
            ApiV1KubernetesAppsInstallCreateUninstallationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_uninstalled_error_component import (
            ApiV1KubernetesAppsInstallCreateUninstalledErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesAppsInstallCreateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateSourceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateByoaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateNamespaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateHaEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateInstalledVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateInstalledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateUninstalledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateInstallationRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateUninstallationRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateInstallationFailedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateUninstallationFailedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateLastInstallationErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateLastMetricsCheckErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreatePodsTotalErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreatePodsReadyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreatePodsAvailableErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreatePodsUnavailableErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreatePodsRestartCountTotalErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreatePodsRestartCountLastHourErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreatePodsDetailsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreatePodsStatusHashErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreatePodsStatusUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateExcludedFromDowntimeUntilErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateCreatedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateHelmChartErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateArtifactPackageErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateArtifactErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsInstallCreateCatalogueAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_kubernetes_apps_install_create_active_error_component import (
            ApiV1KubernetesAppsInstallCreateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_actual_availability_error_component import (
            ApiV1KubernetesAppsInstallCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_annotations_error_component import (
            ApiV1KubernetesAppsInstallCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_archived_at_error_component import (
            ApiV1KubernetesAppsInstallCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_archived_by_error_component import (
            ApiV1KubernetesAppsInstallCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_archived_error_component import (
            ApiV1KubernetesAppsInstallCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_archived_reason_error_component import (
            ApiV1KubernetesAppsInstallCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_artifact_error_component import (
            ApiV1KubernetesAppsInstallCreateArtifactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_artifact_package_error_component import (
            ApiV1KubernetesAppsInstallCreateArtifactPackageErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_block_error_component import (
            ApiV1KubernetesAppsInstallCreateBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_byoa_error_component import (
            ApiV1KubernetesAppsInstallCreateByoaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_catalogue_app_error_component import (
            ApiV1KubernetesAppsInstallCreateCatalogueAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_created_by_component_error_component import (
            ApiV1KubernetesAppsInstallCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_created_by_user_error_component import (
            ApiV1KubernetesAppsInstallCreateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_criticality_error_component import (
            ApiV1KubernetesAppsInstallCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_debug_mode_error_component import (
            ApiV1KubernetesAppsInstallCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_description_error_component import (
            ApiV1KubernetesAppsInstallCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_discovery_enabled_error_component import (
            ApiV1KubernetesAppsInstallCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_display_name_error_component import (
            ApiV1KubernetesAppsInstallCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_excluded_from_downtime_until_error_component import (
            ApiV1KubernetesAppsInstallCreateExcludedFromDowntimeUntilErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_ha_enabled_error_component import (
            ApiV1KubernetesAppsInstallCreateHaEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_helm_chart_error_component import (
            ApiV1KubernetesAppsInstallCreateHelmChartErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_installation_failed_error_component import (
            ApiV1KubernetesAppsInstallCreateInstallationFailedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_installation_running_error_component import (
            ApiV1KubernetesAppsInstallCreateInstallationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_installed_error_component import (
            ApiV1KubernetesAppsInstallCreateInstalledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_installed_version_error_component import (
            ApiV1KubernetesAppsInstallCreateInstalledVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_k8s_cluster_error_component import (
            ApiV1KubernetesAppsInstallCreateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_kind_error_component import (
            ApiV1KubernetesAppsInstallCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_labels_error_component import (
            ApiV1KubernetesAppsInstallCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_last_installation_error_component import (
            ApiV1KubernetesAppsInstallCreateLastInstallationErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_last_metrics_check_error_component import (
            ApiV1KubernetesAppsInstallCreateLastMetricsCheckErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1KubernetesAppsInstallCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_managed_by_content_type_error_component import (
            ApiV1KubernetesAppsInstallCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_managed_by_object_id_error_component import (
            ApiV1KubernetesAppsInstallCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_modified_by_user_error_component import (
            ApiV1KubernetesAppsInstallCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_name_error_component import (
            ApiV1KubernetesAppsInstallCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_namespace_error_component import (
            ApiV1KubernetesAppsInstallCreateNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_non_field_errors_error_component import (
            ApiV1KubernetesAppsInstallCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_platform_dns_record_created_error_component import (
            ApiV1KubernetesAppsInstallCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_platform_service_error_component import (
            ApiV1KubernetesAppsInstallCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_pods_available_error_component import (
            ApiV1KubernetesAppsInstallCreatePodsAvailableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_pods_details_error_component import (
            ApiV1KubernetesAppsInstallCreatePodsDetailsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_pods_ready_error_component import (
            ApiV1KubernetesAppsInstallCreatePodsReadyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_pods_restart_count_last_hour_error_component import (
            ApiV1KubernetesAppsInstallCreatePodsRestartCountLastHourErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_pods_restart_count_total_error_component import (
            ApiV1KubernetesAppsInstallCreatePodsRestartCountTotalErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_pods_status_hash_error_component import (
            ApiV1KubernetesAppsInstallCreatePodsStatusHashErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_pods_status_updated_at_error_component import (
            ApiV1KubernetesAppsInstallCreatePodsStatusUpdatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_pods_total_error_component import (
            ApiV1KubernetesAppsInstallCreatePodsTotalErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_pods_unavailable_error_component import (
            ApiV1KubernetesAppsInstallCreatePodsUnavailableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_provider_error_component import (
            ApiV1KubernetesAppsInstallCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_provider_id_error_component import (
            ApiV1KubernetesAppsInstallCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_provider_reference_error_component import (
            ApiV1KubernetesAppsInstallCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesAppsInstallCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_scope_error_component import (
            ApiV1KubernetesAppsInstallCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_sla_availability_error_component import (
            ApiV1KubernetesAppsInstallCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_sla_target_error_component import (
            ApiV1KubernetesAppsInstallCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_sla_window_days_error_component import (
            ApiV1KubernetesAppsInstallCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_slo_availability_error_component import (
            ApiV1KubernetesAppsInstallCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_slo_target_error_component import (
            ApiV1KubernetesAppsInstallCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_slo_window_days_error_component import (
            ApiV1KubernetesAppsInstallCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_source_error_component import (
            ApiV1KubernetesAppsInstallCreateSourceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_target_availability_error_component import (
            ApiV1KubernetesAppsInstallCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_uninstallation_failed_error_component import (
            ApiV1KubernetesAppsInstallCreateUninstallationFailedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_uninstallation_running_error_component import (
            ApiV1KubernetesAppsInstallCreateUninstallationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_install_create_uninstalled_error_component import (
            ApiV1KubernetesAppsInstallCreateUninstalledErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesAppsInstallCreateActiveErrorComponent
                | ApiV1KubernetesAppsInstallCreateActualAvailabilityErrorComponent
                | ApiV1KubernetesAppsInstallCreateAnnotationsErrorComponent
                | ApiV1KubernetesAppsInstallCreateArchivedAtErrorComponent
                | ApiV1KubernetesAppsInstallCreateArchivedByErrorComponent
                | ApiV1KubernetesAppsInstallCreateArchivedErrorComponent
                | ApiV1KubernetesAppsInstallCreateArchivedReasonErrorComponent
                | ApiV1KubernetesAppsInstallCreateArtifactErrorComponent
                | ApiV1KubernetesAppsInstallCreateArtifactPackageErrorComponent
                | ApiV1KubernetesAppsInstallCreateBlockErrorComponent
                | ApiV1KubernetesAppsInstallCreateByoaErrorComponent
                | ApiV1KubernetesAppsInstallCreateCatalogueAppErrorComponent
                | ApiV1KubernetesAppsInstallCreateCreatedByComponentErrorComponent
                | ApiV1KubernetesAppsInstallCreateCreatedByUserErrorComponent
                | ApiV1KubernetesAppsInstallCreateCriticalityErrorComponent
                | ApiV1KubernetesAppsInstallCreateDebugModeErrorComponent
                | ApiV1KubernetesAppsInstallCreateDescriptionErrorComponent
                | ApiV1KubernetesAppsInstallCreateDiscoveryEnabledErrorComponent
                | ApiV1KubernetesAppsInstallCreateDisplayNameErrorComponent
                | ApiV1KubernetesAppsInstallCreateExcludedFromDowntimeUntilErrorComponent
                | ApiV1KubernetesAppsInstallCreateHaEnabledErrorComponent
                | ApiV1KubernetesAppsInstallCreateHelmChartErrorComponent
                | ApiV1KubernetesAppsInstallCreateInstallationFailedErrorComponent
                | ApiV1KubernetesAppsInstallCreateInstallationRunningErrorComponent
                | ApiV1KubernetesAppsInstallCreateInstalledErrorComponent
                | ApiV1KubernetesAppsInstallCreateInstalledVersionErrorComponent
                | ApiV1KubernetesAppsInstallCreateK8SClusterErrorComponent
                | ApiV1KubernetesAppsInstallCreateKindErrorComponent
                | ApiV1KubernetesAppsInstallCreateLabelsErrorComponent
                | ApiV1KubernetesAppsInstallCreateLastInstallationErrorComponent
                | ApiV1KubernetesAppsInstallCreateLastMetricsCheckErrorComponent
                | ApiV1KubernetesAppsInstallCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1KubernetesAppsInstallCreateManagedByContentTypeErrorComponent
                | ApiV1KubernetesAppsInstallCreateManagedByObjectIdErrorComponent
                | ApiV1KubernetesAppsInstallCreateModifiedByUserErrorComponent
                | ApiV1KubernetesAppsInstallCreateNameErrorComponent
                | ApiV1KubernetesAppsInstallCreateNamespaceErrorComponent
                | ApiV1KubernetesAppsInstallCreateNonFieldErrorsErrorComponent
                | ApiV1KubernetesAppsInstallCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1KubernetesAppsInstallCreatePlatformServiceErrorComponent
                | ApiV1KubernetesAppsInstallCreatePodsAvailableErrorComponent
                | ApiV1KubernetesAppsInstallCreatePodsDetailsErrorComponent
                | ApiV1KubernetesAppsInstallCreatePodsReadyErrorComponent
                | ApiV1KubernetesAppsInstallCreatePodsRestartCountLastHourErrorComponent
                | ApiV1KubernetesAppsInstallCreatePodsRestartCountTotalErrorComponent
                | ApiV1KubernetesAppsInstallCreatePodsStatusHashErrorComponent
                | ApiV1KubernetesAppsInstallCreatePodsStatusUpdatedAtErrorComponent
                | ApiV1KubernetesAppsInstallCreatePodsTotalErrorComponent
                | ApiV1KubernetesAppsInstallCreatePodsUnavailableErrorComponent
                | ApiV1KubernetesAppsInstallCreateProviderErrorComponent
                | ApiV1KubernetesAppsInstallCreateProviderIdErrorComponent
                | ApiV1KubernetesAppsInstallCreateProviderReferenceErrorComponent
                | ApiV1KubernetesAppsInstallCreateReconciliationEnabledErrorComponent
                | ApiV1KubernetesAppsInstallCreateScopeErrorComponent
                | ApiV1KubernetesAppsInstallCreateSlaAvailabilityErrorComponent
                | ApiV1KubernetesAppsInstallCreateSlaTargetErrorComponent
                | ApiV1KubernetesAppsInstallCreateSlaWindowDaysErrorComponent
                | ApiV1KubernetesAppsInstallCreateSloAvailabilityErrorComponent
                | ApiV1KubernetesAppsInstallCreateSloTargetErrorComponent
                | ApiV1KubernetesAppsInstallCreateSloWindowDaysErrorComponent
                | ApiV1KubernetesAppsInstallCreateSourceErrorComponent
                | ApiV1KubernetesAppsInstallCreateTargetAvailabilityErrorComponent
                | ApiV1KubernetesAppsInstallCreateUninstallationFailedErrorComponent
                | ApiV1KubernetesAppsInstallCreateUninstallationRunningErrorComponent
                | ApiV1KubernetesAppsInstallCreateUninstalledErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_0 = (
                        ApiV1KubernetesAppsInstallCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_1 = (
                        ApiV1KubernetesAppsInstallCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_2 = (
                        ApiV1KubernetesAppsInstallCreateBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_3 = (
                        ApiV1KubernetesAppsInstallCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_4 = (
                        ApiV1KubernetesAppsInstallCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_5 = (
                        ApiV1KubernetesAppsInstallCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_6 = (
                        ApiV1KubernetesAppsInstallCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_7 = (
                        ApiV1KubernetesAppsInstallCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_8 = (
                        ApiV1KubernetesAppsInstallCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_9 = (
                        ApiV1KubernetesAppsInstallCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_10 = (
                        ApiV1KubernetesAppsInstallCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_11 = (
                        ApiV1KubernetesAppsInstallCreateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_12 = (
                        ApiV1KubernetesAppsInstallCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_13 = (
                        ApiV1KubernetesAppsInstallCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_14 = (
                        ApiV1KubernetesAppsInstallCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_15 = (
                        ApiV1KubernetesAppsInstallCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_16 = (
                        ApiV1KubernetesAppsInstallCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_17 = (
                        ApiV1KubernetesAppsInstallCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_18 = (
                        ApiV1KubernetesAppsInstallCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_19 = (
                        ApiV1KubernetesAppsInstallCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_20 = (
                        ApiV1KubernetesAppsInstallCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_21 = (
                        ApiV1KubernetesAppsInstallCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_22 = (
                        ApiV1KubernetesAppsInstallCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_23 = (
                        ApiV1KubernetesAppsInstallCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_24 = (
                        ApiV1KubernetesAppsInstallCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_25 = (
                        ApiV1KubernetesAppsInstallCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_26 = (
                        ApiV1KubernetesAppsInstallCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_27 = (
                        ApiV1KubernetesAppsInstallCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_28 = (
                        ApiV1KubernetesAppsInstallCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_29 = (
                        ApiV1KubernetesAppsInstallCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_30 = (
                        ApiV1KubernetesAppsInstallCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_31 = (
                        ApiV1KubernetesAppsInstallCreateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_32 = (
                        ApiV1KubernetesAppsInstallCreateSourceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_33 = (
                        ApiV1KubernetesAppsInstallCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_34 = (
                        ApiV1KubernetesAppsInstallCreateByoaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_35 = (
                        ApiV1KubernetesAppsInstallCreateNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_36 = (
                        ApiV1KubernetesAppsInstallCreateHaEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_37 = (
                        ApiV1KubernetesAppsInstallCreateInstalledVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_38 = (
                        ApiV1KubernetesAppsInstallCreateInstalledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_39 = (
                        ApiV1KubernetesAppsInstallCreateUninstalledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_40 = (
                        ApiV1KubernetesAppsInstallCreateInstallationRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_41 = (
                        ApiV1KubernetesAppsInstallCreateUninstallationRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_42 = (
                        ApiV1KubernetesAppsInstallCreateInstallationFailedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_43 = (
                        ApiV1KubernetesAppsInstallCreateUninstallationFailedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_44 = (
                        ApiV1KubernetesAppsInstallCreateLastInstallationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_45 = (
                        ApiV1KubernetesAppsInstallCreateLastMetricsCheckErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_46 = (
                        ApiV1KubernetesAppsInstallCreatePodsTotalErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_47 = (
                        ApiV1KubernetesAppsInstallCreatePodsReadyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_48 = (
                        ApiV1KubernetesAppsInstallCreatePodsAvailableErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_49 = (
                        ApiV1KubernetesAppsInstallCreatePodsUnavailableErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_50 = (
                        ApiV1KubernetesAppsInstallCreatePodsRestartCountTotalErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_51 = (
                        ApiV1KubernetesAppsInstallCreatePodsRestartCountLastHourErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_52 = (
                        ApiV1KubernetesAppsInstallCreatePodsDetailsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_53 = (
                        ApiV1KubernetesAppsInstallCreatePodsStatusHashErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_54 = (
                        ApiV1KubernetesAppsInstallCreatePodsStatusUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_54
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_55 = (
                        ApiV1KubernetesAppsInstallCreateExcludedFromDowntimeUntilErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_55
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_56 = (
                        ApiV1KubernetesAppsInstallCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_56
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_57 = (
                        ApiV1KubernetesAppsInstallCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_57
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_58 = (
                        ApiV1KubernetesAppsInstallCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_58
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_59 = (
                        ApiV1KubernetesAppsInstallCreateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_59
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_60 = (
                        ApiV1KubernetesAppsInstallCreateHelmChartErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_60
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_61 = (
                        ApiV1KubernetesAppsInstallCreateArtifactPackageErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_61
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_62 = (
                        ApiV1KubernetesAppsInstallCreateArtifactErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_62
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_install_create_error_type_63 = (
                        ApiV1KubernetesAppsInstallCreateCatalogueAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_63
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_apps_install_create_error_type_64 = (
                    ApiV1KubernetesAppsInstallCreateK8SClusterErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_apps_install_create_error_type_64

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_apps_install_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_apps_install_create_validation_error.additional_properties = d
        return api_v1_kubernetes_apps_install_create_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
