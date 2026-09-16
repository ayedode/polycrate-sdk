from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_apps_discover_create_active_error_component import (
        ApiV1KubernetesAppsDiscoverCreateActiveErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_actual_availability_error_component import (
        ApiV1KubernetesAppsDiscoverCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_annotations_error_component import (
        ApiV1KubernetesAppsDiscoverCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_archived_at_error_component import (
        ApiV1KubernetesAppsDiscoverCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_archived_by_error_component import (
        ApiV1KubernetesAppsDiscoverCreateArchivedByErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_archived_error_component import (
        ApiV1KubernetesAppsDiscoverCreateArchivedErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_archived_reason_error_component import (
        ApiV1KubernetesAppsDiscoverCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_artifact_error_component import (
        ApiV1KubernetesAppsDiscoverCreateArtifactErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_artifact_package_error_component import (
        ApiV1KubernetesAppsDiscoverCreateArtifactPackageErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_block_error_component import (
        ApiV1KubernetesAppsDiscoverCreateBlockErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_byoa_error_component import (
        ApiV1KubernetesAppsDiscoverCreateByoaErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_catalogue_app_error_component import (
        ApiV1KubernetesAppsDiscoverCreateCatalogueAppErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_created_by_component_error_component import (
        ApiV1KubernetesAppsDiscoverCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_created_by_user_error_component import (
        ApiV1KubernetesAppsDiscoverCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_criticality_error_component import (
        ApiV1KubernetesAppsDiscoverCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_debug_mode_error_component import (
        ApiV1KubernetesAppsDiscoverCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_description_error_component import (
        ApiV1KubernetesAppsDiscoverCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_discovery_enabled_error_component import (
        ApiV1KubernetesAppsDiscoverCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_display_name_error_component import (
        ApiV1KubernetesAppsDiscoverCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_excluded_from_downtime_until_error_component import (
        ApiV1KubernetesAppsDiscoverCreateExcludedFromDowntimeUntilErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_ha_enabled_error_component import (
        ApiV1KubernetesAppsDiscoverCreateHaEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_helm_chart_error_component import (
        ApiV1KubernetesAppsDiscoverCreateHelmChartErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_installation_failed_error_component import (
        ApiV1KubernetesAppsDiscoverCreateInstallationFailedErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_installation_running_error_component import (
        ApiV1KubernetesAppsDiscoverCreateInstallationRunningErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_installed_error_component import (
        ApiV1KubernetesAppsDiscoverCreateInstalledErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_installed_version_error_component import (
        ApiV1KubernetesAppsDiscoverCreateInstalledVersionErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_k8s_cluster_error_component import (
        ApiV1KubernetesAppsDiscoverCreateK8SClusterErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_kind_error_component import (
        ApiV1KubernetesAppsDiscoverCreateKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_labels_error_component import (
        ApiV1KubernetesAppsDiscoverCreateLabelsErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_last_installation_error_component import (
        ApiV1KubernetesAppsDiscoverCreateLastInstallationErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_last_metrics_check_error_component import (
        ApiV1KubernetesAppsDiscoverCreateLastMetricsCheckErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1KubernetesAppsDiscoverCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_managed_by_content_type_error_component import (
        ApiV1KubernetesAppsDiscoverCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_managed_by_object_id_error_component import (
        ApiV1KubernetesAppsDiscoverCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_modified_by_user_error_component import (
        ApiV1KubernetesAppsDiscoverCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_name_error_component import (
        ApiV1KubernetesAppsDiscoverCreateNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_namespace_error_component import (
        ApiV1KubernetesAppsDiscoverCreateNamespaceErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_non_field_errors_error_component import (
        ApiV1KubernetesAppsDiscoverCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_platform_dns_record_created_error_component import (
        ApiV1KubernetesAppsDiscoverCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_platform_service_error_component import (
        ApiV1KubernetesAppsDiscoverCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_pods_available_error_component import (
        ApiV1KubernetesAppsDiscoverCreatePodsAvailableErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_pods_details_error_component import (
        ApiV1KubernetesAppsDiscoverCreatePodsDetailsErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_pods_ready_error_component import (
        ApiV1KubernetesAppsDiscoverCreatePodsReadyErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_pods_restart_count_last_hour_error_component import (
        ApiV1KubernetesAppsDiscoverCreatePodsRestartCountLastHourErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_pods_restart_count_total_error_component import (
        ApiV1KubernetesAppsDiscoverCreatePodsRestartCountTotalErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_pods_status_hash_error_component import (
        ApiV1KubernetesAppsDiscoverCreatePodsStatusHashErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_pods_status_updated_at_error_component import (
        ApiV1KubernetesAppsDiscoverCreatePodsStatusUpdatedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_pods_total_error_component import (
        ApiV1KubernetesAppsDiscoverCreatePodsTotalErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_pods_unavailable_error_component import (
        ApiV1KubernetesAppsDiscoverCreatePodsUnavailableErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_provider_error_component import (
        ApiV1KubernetesAppsDiscoverCreateProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_provider_id_error_component import (
        ApiV1KubernetesAppsDiscoverCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_provider_reference_error_component import (
        ApiV1KubernetesAppsDiscoverCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_reconciliation_enabled_error_component import (
        ApiV1KubernetesAppsDiscoverCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_scope_error_component import (
        ApiV1KubernetesAppsDiscoverCreateScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_sla_availability_error_component import (
        ApiV1KubernetesAppsDiscoverCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_sla_target_error_component import (
        ApiV1KubernetesAppsDiscoverCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_sla_window_days_error_component import (
        ApiV1KubernetesAppsDiscoverCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_slo_availability_error_component import (
        ApiV1KubernetesAppsDiscoverCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_slo_target_error_component import (
        ApiV1KubernetesAppsDiscoverCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_slo_window_days_error_component import (
        ApiV1KubernetesAppsDiscoverCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_source_error_component import (
        ApiV1KubernetesAppsDiscoverCreateSourceErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_target_availability_error_component import (
        ApiV1KubernetesAppsDiscoverCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_uninstallation_failed_error_component import (
        ApiV1KubernetesAppsDiscoverCreateUninstallationFailedErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_uninstallation_running_error_component import (
        ApiV1KubernetesAppsDiscoverCreateUninstallationRunningErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_discover_create_uninstalled_error_component import (
        ApiV1KubernetesAppsDiscoverCreateUninstalledErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesAppsDiscoverCreateValidationError")


@_attrs_define
class ApiV1KubernetesAppsDiscoverCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesAppsDiscoverCreateActiveErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateActualAvailabilityErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateAnnotationsErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateArchivedAtErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateArchivedByErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateArchivedErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateArchivedReasonErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateArtifactErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateArtifactPackageErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateBlockErrorComponent | ApiV1KubernetesAppsDiscoverCreateByoaErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateCatalogueAppErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateCreatedByComponentErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateCreatedByUserErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateCriticalityErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateDebugModeErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateDescriptionErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateDiscoveryEnabledErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateDisplayNameErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateExcludedFromDowntimeUntilErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateHaEnabledErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateHelmChartErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateInstallationFailedErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateInstallationRunningErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateInstalledErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateInstalledVersionErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateK8SClusterErrorComponent | ApiV1KubernetesAppsDiscoverCreateKindErrorComponent
            | ApiV1KubernetesAppsDiscoverCreateLabelsErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateLastInstallationErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateLastMetricsCheckErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateManagedByContentTypeErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateManagedByObjectIdErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateModifiedByUserErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateNameErrorComponent | ApiV1KubernetesAppsDiscoverCreateNamespaceErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateNonFieldErrorsErrorComponent |
            ApiV1KubernetesAppsDiscoverCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1KubernetesAppsDiscoverCreatePlatformServiceErrorComponent |
            ApiV1KubernetesAppsDiscoverCreatePodsAvailableErrorComponent |
            ApiV1KubernetesAppsDiscoverCreatePodsDetailsErrorComponent |
            ApiV1KubernetesAppsDiscoverCreatePodsReadyErrorComponent |
            ApiV1KubernetesAppsDiscoverCreatePodsRestartCountLastHourErrorComponent |
            ApiV1KubernetesAppsDiscoverCreatePodsRestartCountTotalErrorComponent |
            ApiV1KubernetesAppsDiscoverCreatePodsStatusHashErrorComponent |
            ApiV1KubernetesAppsDiscoverCreatePodsStatusUpdatedAtErrorComponent |
            ApiV1KubernetesAppsDiscoverCreatePodsTotalErrorComponent |
            ApiV1KubernetesAppsDiscoverCreatePodsUnavailableErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateProviderErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateProviderIdErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateProviderReferenceErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateReconciliationEnabledErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateScopeErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateSlaAvailabilityErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateSlaTargetErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateSlaWindowDaysErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateSloAvailabilityErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateSloTargetErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateSloWindowDaysErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateSourceErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateTargetAvailabilityErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateUninstallationFailedErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateUninstallationRunningErrorComponent |
            ApiV1KubernetesAppsDiscoverCreateUninstalledErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesAppsDiscoverCreateActiveErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateActualAvailabilityErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateAnnotationsErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateArchivedAtErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateArchivedByErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateArchivedErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateArchivedReasonErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateArtifactErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateArtifactPackageErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateBlockErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateByoaErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateCatalogueAppErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateCreatedByComponentErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateCreatedByUserErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateCriticalityErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateDebugModeErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateDescriptionErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateDiscoveryEnabledErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateDisplayNameErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateExcludedFromDowntimeUntilErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateHaEnabledErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateHelmChartErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateInstallationFailedErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateInstallationRunningErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateInstalledErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateInstalledVersionErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateK8SClusterErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateKindErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateLabelsErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateLastInstallationErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateLastMetricsCheckErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateManagedByContentTypeErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateManagedByObjectIdErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateModifiedByUserErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateNameErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateNamespaceErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateNonFieldErrorsErrorComponent
        | ApiV1KubernetesAppsDiscoverCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1KubernetesAppsDiscoverCreatePlatformServiceErrorComponent
        | ApiV1KubernetesAppsDiscoverCreatePodsAvailableErrorComponent
        | ApiV1KubernetesAppsDiscoverCreatePodsDetailsErrorComponent
        | ApiV1KubernetesAppsDiscoverCreatePodsReadyErrorComponent
        | ApiV1KubernetesAppsDiscoverCreatePodsRestartCountLastHourErrorComponent
        | ApiV1KubernetesAppsDiscoverCreatePodsRestartCountTotalErrorComponent
        | ApiV1KubernetesAppsDiscoverCreatePodsStatusHashErrorComponent
        | ApiV1KubernetesAppsDiscoverCreatePodsStatusUpdatedAtErrorComponent
        | ApiV1KubernetesAppsDiscoverCreatePodsTotalErrorComponent
        | ApiV1KubernetesAppsDiscoverCreatePodsUnavailableErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateProviderErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateProviderIdErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateProviderReferenceErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateReconciliationEnabledErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateScopeErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateSlaAvailabilityErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateSlaTargetErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateSlaWindowDaysErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateSloAvailabilityErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateSloTargetErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateSloWindowDaysErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateSourceErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateTargetAvailabilityErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateUninstallationFailedErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateUninstallationRunningErrorComponent
        | ApiV1KubernetesAppsDiscoverCreateUninstalledErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_apps_discover_create_active_error_component import (
            ApiV1KubernetesAppsDiscoverCreateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_actual_availability_error_component import (
            ApiV1KubernetesAppsDiscoverCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_annotations_error_component import (
            ApiV1KubernetesAppsDiscoverCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_archived_at_error_component import (
            ApiV1KubernetesAppsDiscoverCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_archived_by_error_component import (
            ApiV1KubernetesAppsDiscoverCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_archived_error_component import (
            ApiV1KubernetesAppsDiscoverCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_archived_reason_error_component import (
            ApiV1KubernetesAppsDiscoverCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_artifact_error_component import (
            ApiV1KubernetesAppsDiscoverCreateArtifactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_artifact_package_error_component import (
            ApiV1KubernetesAppsDiscoverCreateArtifactPackageErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_block_error_component import (
            ApiV1KubernetesAppsDiscoverCreateBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_byoa_error_component import (
            ApiV1KubernetesAppsDiscoverCreateByoaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_catalogue_app_error_component import (
            ApiV1KubernetesAppsDiscoverCreateCatalogueAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_created_by_component_error_component import (
            ApiV1KubernetesAppsDiscoverCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_created_by_user_error_component import (
            ApiV1KubernetesAppsDiscoverCreateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_criticality_error_component import (
            ApiV1KubernetesAppsDiscoverCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_debug_mode_error_component import (
            ApiV1KubernetesAppsDiscoverCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_description_error_component import (
            ApiV1KubernetesAppsDiscoverCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_discovery_enabled_error_component import (
            ApiV1KubernetesAppsDiscoverCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_display_name_error_component import (
            ApiV1KubernetesAppsDiscoverCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_excluded_from_downtime_until_error_component import (
            ApiV1KubernetesAppsDiscoverCreateExcludedFromDowntimeUntilErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_ha_enabled_error_component import (
            ApiV1KubernetesAppsDiscoverCreateHaEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_helm_chart_error_component import (
            ApiV1KubernetesAppsDiscoverCreateHelmChartErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_installation_failed_error_component import (
            ApiV1KubernetesAppsDiscoverCreateInstallationFailedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_installation_running_error_component import (
            ApiV1KubernetesAppsDiscoverCreateInstallationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_installed_error_component import (
            ApiV1KubernetesAppsDiscoverCreateInstalledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_installed_version_error_component import (
            ApiV1KubernetesAppsDiscoverCreateInstalledVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_kind_error_component import (
            ApiV1KubernetesAppsDiscoverCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_labels_error_component import (
            ApiV1KubernetesAppsDiscoverCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_last_installation_error_component import (
            ApiV1KubernetesAppsDiscoverCreateLastInstallationErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_last_metrics_check_error_component import (
            ApiV1KubernetesAppsDiscoverCreateLastMetricsCheckErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1KubernetesAppsDiscoverCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_managed_by_content_type_error_component import (
            ApiV1KubernetesAppsDiscoverCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_managed_by_object_id_error_component import (
            ApiV1KubernetesAppsDiscoverCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_modified_by_user_error_component import (
            ApiV1KubernetesAppsDiscoverCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_name_error_component import (
            ApiV1KubernetesAppsDiscoverCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_namespace_error_component import (
            ApiV1KubernetesAppsDiscoverCreateNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_non_field_errors_error_component import (
            ApiV1KubernetesAppsDiscoverCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_platform_dns_record_created_error_component import (
            ApiV1KubernetesAppsDiscoverCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_platform_service_error_component import (
            ApiV1KubernetesAppsDiscoverCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_pods_available_error_component import (
            ApiV1KubernetesAppsDiscoverCreatePodsAvailableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_pods_details_error_component import (
            ApiV1KubernetesAppsDiscoverCreatePodsDetailsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_pods_ready_error_component import (
            ApiV1KubernetesAppsDiscoverCreatePodsReadyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_pods_restart_count_last_hour_error_component import (
            ApiV1KubernetesAppsDiscoverCreatePodsRestartCountLastHourErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_pods_restart_count_total_error_component import (
            ApiV1KubernetesAppsDiscoverCreatePodsRestartCountTotalErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_pods_status_hash_error_component import (
            ApiV1KubernetesAppsDiscoverCreatePodsStatusHashErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_pods_status_updated_at_error_component import (
            ApiV1KubernetesAppsDiscoverCreatePodsStatusUpdatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_pods_total_error_component import (
            ApiV1KubernetesAppsDiscoverCreatePodsTotalErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_pods_unavailable_error_component import (
            ApiV1KubernetesAppsDiscoverCreatePodsUnavailableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_provider_error_component import (
            ApiV1KubernetesAppsDiscoverCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_provider_id_error_component import (
            ApiV1KubernetesAppsDiscoverCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_provider_reference_error_component import (
            ApiV1KubernetesAppsDiscoverCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesAppsDiscoverCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_scope_error_component import (
            ApiV1KubernetesAppsDiscoverCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_sla_availability_error_component import (
            ApiV1KubernetesAppsDiscoverCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_sla_target_error_component import (
            ApiV1KubernetesAppsDiscoverCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_sla_window_days_error_component import (
            ApiV1KubernetesAppsDiscoverCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_slo_availability_error_component import (
            ApiV1KubernetesAppsDiscoverCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_slo_target_error_component import (
            ApiV1KubernetesAppsDiscoverCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_slo_window_days_error_component import (
            ApiV1KubernetesAppsDiscoverCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_source_error_component import (
            ApiV1KubernetesAppsDiscoverCreateSourceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_target_availability_error_component import (
            ApiV1KubernetesAppsDiscoverCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_uninstallation_failed_error_component import (
            ApiV1KubernetesAppsDiscoverCreateUninstallationFailedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_uninstallation_running_error_component import (
            ApiV1KubernetesAppsDiscoverCreateUninstallationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_uninstalled_error_component import (
            ApiV1KubernetesAppsDiscoverCreateUninstalledErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesAppsDiscoverCreateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateSourceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateByoaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateNamespaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateHaEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateInstalledVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateInstalledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateUninstalledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateInstallationRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateUninstallationRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateInstallationFailedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateUninstallationFailedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateLastInstallationErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateLastMetricsCheckErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreatePodsTotalErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreatePodsReadyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreatePodsAvailableErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreatePodsUnavailableErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreatePodsRestartCountTotalErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreatePodsRestartCountLastHourErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreatePodsDetailsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreatePodsStatusHashErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreatePodsStatusUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateExcludedFromDowntimeUntilErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateCreatedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateHelmChartErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateArtifactPackageErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateArtifactErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsDiscoverCreateCatalogueAppErrorComponent):
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
        from ..models.api_v1_kubernetes_apps_discover_create_active_error_component import (
            ApiV1KubernetesAppsDiscoverCreateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_actual_availability_error_component import (
            ApiV1KubernetesAppsDiscoverCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_annotations_error_component import (
            ApiV1KubernetesAppsDiscoverCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_archived_at_error_component import (
            ApiV1KubernetesAppsDiscoverCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_archived_by_error_component import (
            ApiV1KubernetesAppsDiscoverCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_archived_error_component import (
            ApiV1KubernetesAppsDiscoverCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_archived_reason_error_component import (
            ApiV1KubernetesAppsDiscoverCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_artifact_error_component import (
            ApiV1KubernetesAppsDiscoverCreateArtifactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_artifact_package_error_component import (
            ApiV1KubernetesAppsDiscoverCreateArtifactPackageErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_block_error_component import (
            ApiV1KubernetesAppsDiscoverCreateBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_byoa_error_component import (
            ApiV1KubernetesAppsDiscoverCreateByoaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_catalogue_app_error_component import (
            ApiV1KubernetesAppsDiscoverCreateCatalogueAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_created_by_component_error_component import (
            ApiV1KubernetesAppsDiscoverCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_created_by_user_error_component import (
            ApiV1KubernetesAppsDiscoverCreateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_criticality_error_component import (
            ApiV1KubernetesAppsDiscoverCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_debug_mode_error_component import (
            ApiV1KubernetesAppsDiscoverCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_description_error_component import (
            ApiV1KubernetesAppsDiscoverCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_discovery_enabled_error_component import (
            ApiV1KubernetesAppsDiscoverCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_display_name_error_component import (
            ApiV1KubernetesAppsDiscoverCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_excluded_from_downtime_until_error_component import (
            ApiV1KubernetesAppsDiscoverCreateExcludedFromDowntimeUntilErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_ha_enabled_error_component import (
            ApiV1KubernetesAppsDiscoverCreateHaEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_helm_chart_error_component import (
            ApiV1KubernetesAppsDiscoverCreateHelmChartErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_installation_failed_error_component import (
            ApiV1KubernetesAppsDiscoverCreateInstallationFailedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_installation_running_error_component import (
            ApiV1KubernetesAppsDiscoverCreateInstallationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_installed_error_component import (
            ApiV1KubernetesAppsDiscoverCreateInstalledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_installed_version_error_component import (
            ApiV1KubernetesAppsDiscoverCreateInstalledVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_k8s_cluster_error_component import (
            ApiV1KubernetesAppsDiscoverCreateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_kind_error_component import (
            ApiV1KubernetesAppsDiscoverCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_labels_error_component import (
            ApiV1KubernetesAppsDiscoverCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_last_installation_error_component import (
            ApiV1KubernetesAppsDiscoverCreateLastInstallationErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_last_metrics_check_error_component import (
            ApiV1KubernetesAppsDiscoverCreateLastMetricsCheckErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1KubernetesAppsDiscoverCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_managed_by_content_type_error_component import (
            ApiV1KubernetesAppsDiscoverCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_managed_by_object_id_error_component import (
            ApiV1KubernetesAppsDiscoverCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_modified_by_user_error_component import (
            ApiV1KubernetesAppsDiscoverCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_name_error_component import (
            ApiV1KubernetesAppsDiscoverCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_namespace_error_component import (
            ApiV1KubernetesAppsDiscoverCreateNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_non_field_errors_error_component import (
            ApiV1KubernetesAppsDiscoverCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_platform_dns_record_created_error_component import (
            ApiV1KubernetesAppsDiscoverCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_platform_service_error_component import (
            ApiV1KubernetesAppsDiscoverCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_pods_available_error_component import (
            ApiV1KubernetesAppsDiscoverCreatePodsAvailableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_pods_details_error_component import (
            ApiV1KubernetesAppsDiscoverCreatePodsDetailsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_pods_ready_error_component import (
            ApiV1KubernetesAppsDiscoverCreatePodsReadyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_pods_restart_count_last_hour_error_component import (
            ApiV1KubernetesAppsDiscoverCreatePodsRestartCountLastHourErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_pods_restart_count_total_error_component import (
            ApiV1KubernetesAppsDiscoverCreatePodsRestartCountTotalErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_pods_status_hash_error_component import (
            ApiV1KubernetesAppsDiscoverCreatePodsStatusHashErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_pods_status_updated_at_error_component import (
            ApiV1KubernetesAppsDiscoverCreatePodsStatusUpdatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_pods_total_error_component import (
            ApiV1KubernetesAppsDiscoverCreatePodsTotalErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_pods_unavailable_error_component import (
            ApiV1KubernetesAppsDiscoverCreatePodsUnavailableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_provider_error_component import (
            ApiV1KubernetesAppsDiscoverCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_provider_id_error_component import (
            ApiV1KubernetesAppsDiscoverCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_provider_reference_error_component import (
            ApiV1KubernetesAppsDiscoverCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesAppsDiscoverCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_scope_error_component import (
            ApiV1KubernetesAppsDiscoverCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_sla_availability_error_component import (
            ApiV1KubernetesAppsDiscoverCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_sla_target_error_component import (
            ApiV1KubernetesAppsDiscoverCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_sla_window_days_error_component import (
            ApiV1KubernetesAppsDiscoverCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_slo_availability_error_component import (
            ApiV1KubernetesAppsDiscoverCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_slo_target_error_component import (
            ApiV1KubernetesAppsDiscoverCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_slo_window_days_error_component import (
            ApiV1KubernetesAppsDiscoverCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_source_error_component import (
            ApiV1KubernetesAppsDiscoverCreateSourceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_target_availability_error_component import (
            ApiV1KubernetesAppsDiscoverCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_uninstallation_failed_error_component import (
            ApiV1KubernetesAppsDiscoverCreateUninstallationFailedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_uninstallation_running_error_component import (
            ApiV1KubernetesAppsDiscoverCreateUninstallationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_discover_create_uninstalled_error_component import (
            ApiV1KubernetesAppsDiscoverCreateUninstalledErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesAppsDiscoverCreateActiveErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateActualAvailabilityErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateAnnotationsErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateArchivedAtErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateArchivedByErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateArchivedErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateArchivedReasonErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateArtifactErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateArtifactPackageErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateBlockErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateByoaErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateCatalogueAppErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateCreatedByComponentErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateCreatedByUserErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateCriticalityErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateDebugModeErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateDescriptionErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateDiscoveryEnabledErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateDisplayNameErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateExcludedFromDowntimeUntilErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateHaEnabledErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateHelmChartErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateInstallationFailedErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateInstallationRunningErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateInstalledErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateInstalledVersionErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateK8SClusterErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateKindErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateLabelsErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateLastInstallationErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateLastMetricsCheckErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateManagedByContentTypeErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateManagedByObjectIdErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateModifiedByUserErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateNameErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateNamespaceErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateNonFieldErrorsErrorComponent
                | ApiV1KubernetesAppsDiscoverCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1KubernetesAppsDiscoverCreatePlatformServiceErrorComponent
                | ApiV1KubernetesAppsDiscoverCreatePodsAvailableErrorComponent
                | ApiV1KubernetesAppsDiscoverCreatePodsDetailsErrorComponent
                | ApiV1KubernetesAppsDiscoverCreatePodsReadyErrorComponent
                | ApiV1KubernetesAppsDiscoverCreatePodsRestartCountLastHourErrorComponent
                | ApiV1KubernetesAppsDiscoverCreatePodsRestartCountTotalErrorComponent
                | ApiV1KubernetesAppsDiscoverCreatePodsStatusHashErrorComponent
                | ApiV1KubernetesAppsDiscoverCreatePodsStatusUpdatedAtErrorComponent
                | ApiV1KubernetesAppsDiscoverCreatePodsTotalErrorComponent
                | ApiV1KubernetesAppsDiscoverCreatePodsUnavailableErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateProviderErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateProviderIdErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateProviderReferenceErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateReconciliationEnabledErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateScopeErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateSlaAvailabilityErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateSlaTargetErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateSlaWindowDaysErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateSloAvailabilityErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateSloTargetErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateSloWindowDaysErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateSourceErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateTargetAvailabilityErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateUninstallationFailedErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateUninstallationRunningErrorComponent
                | ApiV1KubernetesAppsDiscoverCreateUninstalledErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_0 = (
                        ApiV1KubernetesAppsDiscoverCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_1 = (
                        ApiV1KubernetesAppsDiscoverCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_2 = (
                        ApiV1KubernetesAppsDiscoverCreateBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_3 = (
                        ApiV1KubernetesAppsDiscoverCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_4 = (
                        ApiV1KubernetesAppsDiscoverCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_5 = (
                        ApiV1KubernetesAppsDiscoverCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_6 = (
                        ApiV1KubernetesAppsDiscoverCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_7 = (
                        ApiV1KubernetesAppsDiscoverCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_8 = (
                        ApiV1KubernetesAppsDiscoverCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_9 = (
                        ApiV1KubernetesAppsDiscoverCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_10 = (
                        ApiV1KubernetesAppsDiscoverCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_11 = (
                        ApiV1KubernetesAppsDiscoverCreateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_12 = (
                        ApiV1KubernetesAppsDiscoverCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_13 = (
                        ApiV1KubernetesAppsDiscoverCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_14 = (
                        ApiV1KubernetesAppsDiscoverCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_15 = (
                        ApiV1KubernetesAppsDiscoverCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_16 = (
                        ApiV1KubernetesAppsDiscoverCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_17 = (
                        ApiV1KubernetesAppsDiscoverCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_18 = (
                        ApiV1KubernetesAppsDiscoverCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_19 = (
                        ApiV1KubernetesAppsDiscoverCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_20 = (
                        ApiV1KubernetesAppsDiscoverCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_21 = (
                        ApiV1KubernetesAppsDiscoverCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_22 = (
                        ApiV1KubernetesAppsDiscoverCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_23 = (
                        ApiV1KubernetesAppsDiscoverCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_24 = (
                        ApiV1KubernetesAppsDiscoverCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_25 = (
                        ApiV1KubernetesAppsDiscoverCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_26 = (
                        ApiV1KubernetesAppsDiscoverCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_27 = (
                        ApiV1KubernetesAppsDiscoverCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_28 = (
                        ApiV1KubernetesAppsDiscoverCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_29 = (
                        ApiV1KubernetesAppsDiscoverCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_30 = (
                        ApiV1KubernetesAppsDiscoverCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_31 = (
                        ApiV1KubernetesAppsDiscoverCreateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_32 = (
                        ApiV1KubernetesAppsDiscoverCreateSourceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_33 = (
                        ApiV1KubernetesAppsDiscoverCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_34 = (
                        ApiV1KubernetesAppsDiscoverCreateByoaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_35 = (
                        ApiV1KubernetesAppsDiscoverCreateNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_36 = (
                        ApiV1KubernetesAppsDiscoverCreateHaEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_37 = (
                        ApiV1KubernetesAppsDiscoverCreateInstalledVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_38 = (
                        ApiV1KubernetesAppsDiscoverCreateInstalledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_39 = (
                        ApiV1KubernetesAppsDiscoverCreateUninstalledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_40 = (
                        ApiV1KubernetesAppsDiscoverCreateInstallationRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_41 = (
                        ApiV1KubernetesAppsDiscoverCreateUninstallationRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_42 = (
                        ApiV1KubernetesAppsDiscoverCreateInstallationFailedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_43 = (
                        ApiV1KubernetesAppsDiscoverCreateUninstallationFailedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_44 = (
                        ApiV1KubernetesAppsDiscoverCreateLastInstallationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_45 = (
                        ApiV1KubernetesAppsDiscoverCreateLastMetricsCheckErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_46 = (
                        ApiV1KubernetesAppsDiscoverCreatePodsTotalErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_47 = (
                        ApiV1KubernetesAppsDiscoverCreatePodsReadyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_48 = (
                        ApiV1KubernetesAppsDiscoverCreatePodsAvailableErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_49 = (
                        ApiV1KubernetesAppsDiscoverCreatePodsUnavailableErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_50 = (
                        ApiV1KubernetesAppsDiscoverCreatePodsRestartCountTotalErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_51 = (
                        ApiV1KubernetesAppsDiscoverCreatePodsRestartCountLastHourErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_52 = (
                        ApiV1KubernetesAppsDiscoverCreatePodsDetailsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_53 = (
                        ApiV1KubernetesAppsDiscoverCreatePodsStatusHashErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_54 = (
                        ApiV1KubernetesAppsDiscoverCreatePodsStatusUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_54
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_55 = (
                        ApiV1KubernetesAppsDiscoverCreateExcludedFromDowntimeUntilErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_55
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_56 = (
                        ApiV1KubernetesAppsDiscoverCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_56
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_57 = (
                        ApiV1KubernetesAppsDiscoverCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_57
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_58 = (
                        ApiV1KubernetesAppsDiscoverCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_58
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_59 = (
                        ApiV1KubernetesAppsDiscoverCreateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_59
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_60 = (
                        ApiV1KubernetesAppsDiscoverCreateHelmChartErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_60
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_61 = (
                        ApiV1KubernetesAppsDiscoverCreateArtifactPackageErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_61
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_62 = (
                        ApiV1KubernetesAppsDiscoverCreateArtifactErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_62
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_63 = (
                        ApiV1KubernetesAppsDiscoverCreateCatalogueAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_63
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_64 = (
                    ApiV1KubernetesAppsDiscoverCreateK8SClusterErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_apps_discover_create_error_type_64

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_apps_discover_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_apps_discover_create_validation_error.additional_properties = d
        return api_v1_kubernetes_apps_discover_create_validation_error

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
