from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_apps_archive_create_active_error_component import (
        ApiV1KubernetesAppsArchiveCreateActiveErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_actual_availability_error_component import (
        ApiV1KubernetesAppsArchiveCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_annotations_error_component import (
        ApiV1KubernetesAppsArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_archived_at_error_component import (
        ApiV1KubernetesAppsArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_archived_by_error_component import (
        ApiV1KubernetesAppsArchiveCreateArchivedByErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_archived_error_component import (
        ApiV1KubernetesAppsArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_archived_reason_error_component import (
        ApiV1KubernetesAppsArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_artifact_error_component import (
        ApiV1KubernetesAppsArchiveCreateArtifactErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_artifact_package_error_component import (
        ApiV1KubernetesAppsArchiveCreateArtifactPackageErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_block_error_component import (
        ApiV1KubernetesAppsArchiveCreateBlockErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_byoa_error_component import (
        ApiV1KubernetesAppsArchiveCreateByoaErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_catalogue_app_error_component import (
        ApiV1KubernetesAppsArchiveCreateCatalogueAppErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_created_by_component_error_component import (
        ApiV1KubernetesAppsArchiveCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_created_by_user_error_component import (
        ApiV1KubernetesAppsArchiveCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_criticality_error_component import (
        ApiV1KubernetesAppsArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_debug_mode_error_component import (
        ApiV1KubernetesAppsArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_description_error_component import (
        ApiV1KubernetesAppsArchiveCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_discovery_enabled_error_component import (
        ApiV1KubernetesAppsArchiveCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_display_name_error_component import (
        ApiV1KubernetesAppsArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_excluded_from_downtime_until_error_component import (
        ApiV1KubernetesAppsArchiveCreateExcludedFromDowntimeUntilErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_ha_enabled_error_component import (
        ApiV1KubernetesAppsArchiveCreateHaEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_helm_chart_error_component import (
        ApiV1KubernetesAppsArchiveCreateHelmChartErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_installation_failed_error_component import (
        ApiV1KubernetesAppsArchiveCreateInstallationFailedErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_installation_running_error_component import (
        ApiV1KubernetesAppsArchiveCreateInstallationRunningErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_installed_error_component import (
        ApiV1KubernetesAppsArchiveCreateInstalledErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_installed_version_error_component import (
        ApiV1KubernetesAppsArchiveCreateInstalledVersionErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_k8s_cluster_error_component import (
        ApiV1KubernetesAppsArchiveCreateK8SClusterErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_kind_error_component import (
        ApiV1KubernetesAppsArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_labels_error_component import (
        ApiV1KubernetesAppsArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_last_installation_error_component import (
        ApiV1KubernetesAppsArchiveCreateLastInstallationErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_last_metrics_check_error_component import (
        ApiV1KubernetesAppsArchiveCreateLastMetricsCheckErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1KubernetesAppsArchiveCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_managed_by_content_type_error_component import (
        ApiV1KubernetesAppsArchiveCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_managed_by_object_id_error_component import (
        ApiV1KubernetesAppsArchiveCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_modified_by_user_error_component import (
        ApiV1KubernetesAppsArchiveCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_name_error_component import (
        ApiV1KubernetesAppsArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_namespace_error_component import (
        ApiV1KubernetesAppsArchiveCreateNamespaceErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_non_field_errors_error_component import (
        ApiV1KubernetesAppsArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_platform_dns_record_created_error_component import (
        ApiV1KubernetesAppsArchiveCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_platform_service_error_component import (
        ApiV1KubernetesAppsArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_pods_available_error_component import (
        ApiV1KubernetesAppsArchiveCreatePodsAvailableErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_pods_details_error_component import (
        ApiV1KubernetesAppsArchiveCreatePodsDetailsErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_pods_ready_error_component import (
        ApiV1KubernetesAppsArchiveCreatePodsReadyErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_pods_restart_count_last_hour_error_component import (
        ApiV1KubernetesAppsArchiveCreatePodsRestartCountLastHourErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_pods_restart_count_total_error_component import (
        ApiV1KubernetesAppsArchiveCreatePodsRestartCountTotalErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_pods_status_hash_error_component import (
        ApiV1KubernetesAppsArchiveCreatePodsStatusHashErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_pods_status_updated_at_error_component import (
        ApiV1KubernetesAppsArchiveCreatePodsStatusUpdatedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_pods_total_error_component import (
        ApiV1KubernetesAppsArchiveCreatePodsTotalErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_pods_unavailable_error_component import (
        ApiV1KubernetesAppsArchiveCreatePodsUnavailableErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_provider_error_component import (
        ApiV1KubernetesAppsArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_provider_id_error_component import (
        ApiV1KubernetesAppsArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_provider_reference_error_component import (
        ApiV1KubernetesAppsArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_reconciliation_enabled_error_component import (
        ApiV1KubernetesAppsArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_scope_error_component import (
        ApiV1KubernetesAppsArchiveCreateScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_sla_availability_error_component import (
        ApiV1KubernetesAppsArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_sla_target_error_component import (
        ApiV1KubernetesAppsArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_sla_window_days_error_component import (
        ApiV1KubernetesAppsArchiveCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_slo_availability_error_component import (
        ApiV1KubernetesAppsArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_slo_target_error_component import (
        ApiV1KubernetesAppsArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_slo_window_days_error_component import (
        ApiV1KubernetesAppsArchiveCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_source_error_component import (
        ApiV1KubernetesAppsArchiveCreateSourceErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_target_availability_error_component import (
        ApiV1KubernetesAppsArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_uninstallation_failed_error_component import (
        ApiV1KubernetesAppsArchiveCreateUninstallationFailedErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_uninstallation_running_error_component import (
        ApiV1KubernetesAppsArchiveCreateUninstallationRunningErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_archive_create_uninstalled_error_component import (
        ApiV1KubernetesAppsArchiveCreateUninstalledErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesAppsArchiveCreateValidationError")


@_attrs_define
class ApiV1KubernetesAppsArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesAppsArchiveCreateActiveErrorComponent |
            ApiV1KubernetesAppsArchiveCreateActualAvailabilityErrorComponent |
            ApiV1KubernetesAppsArchiveCreateAnnotationsErrorComponent |
            ApiV1KubernetesAppsArchiveCreateArchivedAtErrorComponent |
            ApiV1KubernetesAppsArchiveCreateArchivedByErrorComponent |
            ApiV1KubernetesAppsArchiveCreateArchivedErrorComponent |
            ApiV1KubernetesAppsArchiveCreateArchivedReasonErrorComponent |
            ApiV1KubernetesAppsArchiveCreateArtifactErrorComponent |
            ApiV1KubernetesAppsArchiveCreateArtifactPackageErrorComponent |
            ApiV1KubernetesAppsArchiveCreateBlockErrorComponent | ApiV1KubernetesAppsArchiveCreateByoaErrorComponent |
            ApiV1KubernetesAppsArchiveCreateCatalogueAppErrorComponent |
            ApiV1KubernetesAppsArchiveCreateCreatedByComponentErrorComponent |
            ApiV1KubernetesAppsArchiveCreateCreatedByUserErrorComponent |
            ApiV1KubernetesAppsArchiveCreateCriticalityErrorComponent |
            ApiV1KubernetesAppsArchiveCreateDebugModeErrorComponent |
            ApiV1KubernetesAppsArchiveCreateDescriptionErrorComponent |
            ApiV1KubernetesAppsArchiveCreateDiscoveryEnabledErrorComponent |
            ApiV1KubernetesAppsArchiveCreateDisplayNameErrorComponent |
            ApiV1KubernetesAppsArchiveCreateExcludedFromDowntimeUntilErrorComponent |
            ApiV1KubernetesAppsArchiveCreateHaEnabledErrorComponent |
            ApiV1KubernetesAppsArchiveCreateHelmChartErrorComponent |
            ApiV1KubernetesAppsArchiveCreateInstallationFailedErrorComponent |
            ApiV1KubernetesAppsArchiveCreateInstallationRunningErrorComponent |
            ApiV1KubernetesAppsArchiveCreateInstalledErrorComponent |
            ApiV1KubernetesAppsArchiveCreateInstalledVersionErrorComponent |
            ApiV1KubernetesAppsArchiveCreateK8SClusterErrorComponent | ApiV1KubernetesAppsArchiveCreateKindErrorComponent |
            ApiV1KubernetesAppsArchiveCreateLabelsErrorComponent |
            ApiV1KubernetesAppsArchiveCreateLastInstallationErrorComponent |
            ApiV1KubernetesAppsArchiveCreateLastMetricsCheckErrorComponent |
            ApiV1KubernetesAppsArchiveCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1KubernetesAppsArchiveCreateManagedByContentTypeErrorComponent |
            ApiV1KubernetesAppsArchiveCreateManagedByObjectIdErrorComponent |
            ApiV1KubernetesAppsArchiveCreateModifiedByUserErrorComponent |
            ApiV1KubernetesAppsArchiveCreateNameErrorComponent | ApiV1KubernetesAppsArchiveCreateNamespaceErrorComponent |
            ApiV1KubernetesAppsArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1KubernetesAppsArchiveCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1KubernetesAppsArchiveCreatePlatformServiceErrorComponent |
            ApiV1KubernetesAppsArchiveCreatePodsAvailableErrorComponent |
            ApiV1KubernetesAppsArchiveCreatePodsDetailsErrorComponent |
            ApiV1KubernetesAppsArchiveCreatePodsReadyErrorComponent |
            ApiV1KubernetesAppsArchiveCreatePodsRestartCountLastHourErrorComponent |
            ApiV1KubernetesAppsArchiveCreatePodsRestartCountTotalErrorComponent |
            ApiV1KubernetesAppsArchiveCreatePodsStatusHashErrorComponent |
            ApiV1KubernetesAppsArchiveCreatePodsStatusUpdatedAtErrorComponent |
            ApiV1KubernetesAppsArchiveCreatePodsTotalErrorComponent |
            ApiV1KubernetesAppsArchiveCreatePodsUnavailableErrorComponent |
            ApiV1KubernetesAppsArchiveCreateProviderErrorComponent |
            ApiV1KubernetesAppsArchiveCreateProviderIdErrorComponent |
            ApiV1KubernetesAppsArchiveCreateProviderReferenceErrorComponent |
            ApiV1KubernetesAppsArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1KubernetesAppsArchiveCreateScopeErrorComponent |
            ApiV1KubernetesAppsArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1KubernetesAppsArchiveCreateSlaTargetErrorComponent |
            ApiV1KubernetesAppsArchiveCreateSlaWindowDaysErrorComponent |
            ApiV1KubernetesAppsArchiveCreateSloAvailabilityErrorComponent |
            ApiV1KubernetesAppsArchiveCreateSloTargetErrorComponent |
            ApiV1KubernetesAppsArchiveCreateSloWindowDaysErrorComponent |
            ApiV1KubernetesAppsArchiveCreateSourceErrorComponent |
            ApiV1KubernetesAppsArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1KubernetesAppsArchiveCreateUninstallationFailedErrorComponent |
            ApiV1KubernetesAppsArchiveCreateUninstallationRunningErrorComponent |
            ApiV1KubernetesAppsArchiveCreateUninstalledErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesAppsArchiveCreateActiveErrorComponent
        | ApiV1KubernetesAppsArchiveCreateActualAvailabilityErrorComponent
        | ApiV1KubernetesAppsArchiveCreateAnnotationsErrorComponent
        | ApiV1KubernetesAppsArchiveCreateArchivedAtErrorComponent
        | ApiV1KubernetesAppsArchiveCreateArchivedByErrorComponent
        | ApiV1KubernetesAppsArchiveCreateArchivedErrorComponent
        | ApiV1KubernetesAppsArchiveCreateArchivedReasonErrorComponent
        | ApiV1KubernetesAppsArchiveCreateArtifactErrorComponent
        | ApiV1KubernetesAppsArchiveCreateArtifactPackageErrorComponent
        | ApiV1KubernetesAppsArchiveCreateBlockErrorComponent
        | ApiV1KubernetesAppsArchiveCreateByoaErrorComponent
        | ApiV1KubernetesAppsArchiveCreateCatalogueAppErrorComponent
        | ApiV1KubernetesAppsArchiveCreateCreatedByComponentErrorComponent
        | ApiV1KubernetesAppsArchiveCreateCreatedByUserErrorComponent
        | ApiV1KubernetesAppsArchiveCreateCriticalityErrorComponent
        | ApiV1KubernetesAppsArchiveCreateDebugModeErrorComponent
        | ApiV1KubernetesAppsArchiveCreateDescriptionErrorComponent
        | ApiV1KubernetesAppsArchiveCreateDiscoveryEnabledErrorComponent
        | ApiV1KubernetesAppsArchiveCreateDisplayNameErrorComponent
        | ApiV1KubernetesAppsArchiveCreateExcludedFromDowntimeUntilErrorComponent
        | ApiV1KubernetesAppsArchiveCreateHaEnabledErrorComponent
        | ApiV1KubernetesAppsArchiveCreateHelmChartErrorComponent
        | ApiV1KubernetesAppsArchiveCreateInstallationFailedErrorComponent
        | ApiV1KubernetesAppsArchiveCreateInstallationRunningErrorComponent
        | ApiV1KubernetesAppsArchiveCreateInstalledErrorComponent
        | ApiV1KubernetesAppsArchiveCreateInstalledVersionErrorComponent
        | ApiV1KubernetesAppsArchiveCreateK8SClusterErrorComponent
        | ApiV1KubernetesAppsArchiveCreateKindErrorComponent
        | ApiV1KubernetesAppsArchiveCreateLabelsErrorComponent
        | ApiV1KubernetesAppsArchiveCreateLastInstallationErrorComponent
        | ApiV1KubernetesAppsArchiveCreateLastMetricsCheckErrorComponent
        | ApiV1KubernetesAppsArchiveCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1KubernetesAppsArchiveCreateManagedByContentTypeErrorComponent
        | ApiV1KubernetesAppsArchiveCreateManagedByObjectIdErrorComponent
        | ApiV1KubernetesAppsArchiveCreateModifiedByUserErrorComponent
        | ApiV1KubernetesAppsArchiveCreateNameErrorComponent
        | ApiV1KubernetesAppsArchiveCreateNamespaceErrorComponent
        | ApiV1KubernetesAppsArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1KubernetesAppsArchiveCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1KubernetesAppsArchiveCreatePlatformServiceErrorComponent
        | ApiV1KubernetesAppsArchiveCreatePodsAvailableErrorComponent
        | ApiV1KubernetesAppsArchiveCreatePodsDetailsErrorComponent
        | ApiV1KubernetesAppsArchiveCreatePodsReadyErrorComponent
        | ApiV1KubernetesAppsArchiveCreatePodsRestartCountLastHourErrorComponent
        | ApiV1KubernetesAppsArchiveCreatePodsRestartCountTotalErrorComponent
        | ApiV1KubernetesAppsArchiveCreatePodsStatusHashErrorComponent
        | ApiV1KubernetesAppsArchiveCreatePodsStatusUpdatedAtErrorComponent
        | ApiV1KubernetesAppsArchiveCreatePodsTotalErrorComponent
        | ApiV1KubernetesAppsArchiveCreatePodsUnavailableErrorComponent
        | ApiV1KubernetesAppsArchiveCreateProviderErrorComponent
        | ApiV1KubernetesAppsArchiveCreateProviderIdErrorComponent
        | ApiV1KubernetesAppsArchiveCreateProviderReferenceErrorComponent
        | ApiV1KubernetesAppsArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1KubernetesAppsArchiveCreateScopeErrorComponent
        | ApiV1KubernetesAppsArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1KubernetesAppsArchiveCreateSlaTargetErrorComponent
        | ApiV1KubernetesAppsArchiveCreateSlaWindowDaysErrorComponent
        | ApiV1KubernetesAppsArchiveCreateSloAvailabilityErrorComponent
        | ApiV1KubernetesAppsArchiveCreateSloTargetErrorComponent
        | ApiV1KubernetesAppsArchiveCreateSloWindowDaysErrorComponent
        | ApiV1KubernetesAppsArchiveCreateSourceErrorComponent
        | ApiV1KubernetesAppsArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1KubernetesAppsArchiveCreateUninstallationFailedErrorComponent
        | ApiV1KubernetesAppsArchiveCreateUninstallationRunningErrorComponent
        | ApiV1KubernetesAppsArchiveCreateUninstalledErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_apps_archive_create_active_error_component import (
            ApiV1KubernetesAppsArchiveCreateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_actual_availability_error_component import (
            ApiV1KubernetesAppsArchiveCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_annotations_error_component import (
            ApiV1KubernetesAppsArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_archived_at_error_component import (
            ApiV1KubernetesAppsArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_archived_by_error_component import (
            ApiV1KubernetesAppsArchiveCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_archived_error_component import (
            ApiV1KubernetesAppsArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_archived_reason_error_component import (
            ApiV1KubernetesAppsArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_artifact_error_component import (
            ApiV1KubernetesAppsArchiveCreateArtifactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_artifact_package_error_component import (
            ApiV1KubernetesAppsArchiveCreateArtifactPackageErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_block_error_component import (
            ApiV1KubernetesAppsArchiveCreateBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_byoa_error_component import (
            ApiV1KubernetesAppsArchiveCreateByoaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_catalogue_app_error_component import (
            ApiV1KubernetesAppsArchiveCreateCatalogueAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_created_by_component_error_component import (
            ApiV1KubernetesAppsArchiveCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_created_by_user_error_component import (
            ApiV1KubernetesAppsArchiveCreateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_criticality_error_component import (
            ApiV1KubernetesAppsArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_debug_mode_error_component import (
            ApiV1KubernetesAppsArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_description_error_component import (
            ApiV1KubernetesAppsArchiveCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_discovery_enabled_error_component import (
            ApiV1KubernetesAppsArchiveCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_display_name_error_component import (
            ApiV1KubernetesAppsArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_excluded_from_downtime_until_error_component import (
            ApiV1KubernetesAppsArchiveCreateExcludedFromDowntimeUntilErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_ha_enabled_error_component import (
            ApiV1KubernetesAppsArchiveCreateHaEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_helm_chart_error_component import (
            ApiV1KubernetesAppsArchiveCreateHelmChartErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_installation_failed_error_component import (
            ApiV1KubernetesAppsArchiveCreateInstallationFailedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_installation_running_error_component import (
            ApiV1KubernetesAppsArchiveCreateInstallationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_installed_error_component import (
            ApiV1KubernetesAppsArchiveCreateInstalledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_installed_version_error_component import (
            ApiV1KubernetesAppsArchiveCreateInstalledVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_kind_error_component import (
            ApiV1KubernetesAppsArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_labels_error_component import (
            ApiV1KubernetesAppsArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_last_installation_error_component import (
            ApiV1KubernetesAppsArchiveCreateLastInstallationErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_last_metrics_check_error_component import (
            ApiV1KubernetesAppsArchiveCreateLastMetricsCheckErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1KubernetesAppsArchiveCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_managed_by_content_type_error_component import (
            ApiV1KubernetesAppsArchiveCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_managed_by_object_id_error_component import (
            ApiV1KubernetesAppsArchiveCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_modified_by_user_error_component import (
            ApiV1KubernetesAppsArchiveCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_name_error_component import (
            ApiV1KubernetesAppsArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_namespace_error_component import (
            ApiV1KubernetesAppsArchiveCreateNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_non_field_errors_error_component import (
            ApiV1KubernetesAppsArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_platform_dns_record_created_error_component import (
            ApiV1KubernetesAppsArchiveCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_platform_service_error_component import (
            ApiV1KubernetesAppsArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_pods_available_error_component import (
            ApiV1KubernetesAppsArchiveCreatePodsAvailableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_pods_details_error_component import (
            ApiV1KubernetesAppsArchiveCreatePodsDetailsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_pods_ready_error_component import (
            ApiV1KubernetesAppsArchiveCreatePodsReadyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_pods_restart_count_last_hour_error_component import (
            ApiV1KubernetesAppsArchiveCreatePodsRestartCountLastHourErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_pods_restart_count_total_error_component import (
            ApiV1KubernetesAppsArchiveCreatePodsRestartCountTotalErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_pods_status_hash_error_component import (
            ApiV1KubernetesAppsArchiveCreatePodsStatusHashErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_pods_status_updated_at_error_component import (
            ApiV1KubernetesAppsArchiveCreatePodsStatusUpdatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_pods_total_error_component import (
            ApiV1KubernetesAppsArchiveCreatePodsTotalErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_pods_unavailable_error_component import (
            ApiV1KubernetesAppsArchiveCreatePodsUnavailableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_provider_error_component import (
            ApiV1KubernetesAppsArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_provider_id_error_component import (
            ApiV1KubernetesAppsArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_provider_reference_error_component import (
            ApiV1KubernetesAppsArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesAppsArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_scope_error_component import (
            ApiV1KubernetesAppsArchiveCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_sla_availability_error_component import (
            ApiV1KubernetesAppsArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_sla_target_error_component import (
            ApiV1KubernetesAppsArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_sla_window_days_error_component import (
            ApiV1KubernetesAppsArchiveCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_slo_availability_error_component import (
            ApiV1KubernetesAppsArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_slo_target_error_component import (
            ApiV1KubernetesAppsArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_slo_window_days_error_component import (
            ApiV1KubernetesAppsArchiveCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_source_error_component import (
            ApiV1KubernetesAppsArchiveCreateSourceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_target_availability_error_component import (
            ApiV1KubernetesAppsArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_uninstallation_failed_error_component import (
            ApiV1KubernetesAppsArchiveCreateUninstallationFailedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_uninstallation_running_error_component import (
            ApiV1KubernetesAppsArchiveCreateUninstallationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_uninstalled_error_component import (
            ApiV1KubernetesAppsArchiveCreateUninstalledErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesAppsArchiveCreateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateSourceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateByoaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateNamespaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateHaEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateInstalledVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateInstalledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateUninstalledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateInstallationRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateUninstallationRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateInstallationFailedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateUninstallationFailedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateLastInstallationErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateLastMetricsCheckErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreatePodsTotalErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreatePodsReadyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreatePodsAvailableErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreatePodsUnavailableErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreatePodsRestartCountTotalErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreatePodsRestartCountLastHourErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreatePodsDetailsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreatePodsStatusHashErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreatePodsStatusUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateExcludedFromDowntimeUntilErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateCreatedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateHelmChartErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateArtifactPackageErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateArtifactErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsArchiveCreateCatalogueAppErrorComponent):
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
        from ..models.api_v1_kubernetes_apps_archive_create_active_error_component import (
            ApiV1KubernetesAppsArchiveCreateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_actual_availability_error_component import (
            ApiV1KubernetesAppsArchiveCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_annotations_error_component import (
            ApiV1KubernetesAppsArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_archived_at_error_component import (
            ApiV1KubernetesAppsArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_archived_by_error_component import (
            ApiV1KubernetesAppsArchiveCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_archived_error_component import (
            ApiV1KubernetesAppsArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_archived_reason_error_component import (
            ApiV1KubernetesAppsArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_artifact_error_component import (
            ApiV1KubernetesAppsArchiveCreateArtifactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_artifact_package_error_component import (
            ApiV1KubernetesAppsArchiveCreateArtifactPackageErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_block_error_component import (
            ApiV1KubernetesAppsArchiveCreateBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_byoa_error_component import (
            ApiV1KubernetesAppsArchiveCreateByoaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_catalogue_app_error_component import (
            ApiV1KubernetesAppsArchiveCreateCatalogueAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_created_by_component_error_component import (
            ApiV1KubernetesAppsArchiveCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_created_by_user_error_component import (
            ApiV1KubernetesAppsArchiveCreateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_criticality_error_component import (
            ApiV1KubernetesAppsArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_debug_mode_error_component import (
            ApiV1KubernetesAppsArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_description_error_component import (
            ApiV1KubernetesAppsArchiveCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_discovery_enabled_error_component import (
            ApiV1KubernetesAppsArchiveCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_display_name_error_component import (
            ApiV1KubernetesAppsArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_excluded_from_downtime_until_error_component import (
            ApiV1KubernetesAppsArchiveCreateExcludedFromDowntimeUntilErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_ha_enabled_error_component import (
            ApiV1KubernetesAppsArchiveCreateHaEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_helm_chart_error_component import (
            ApiV1KubernetesAppsArchiveCreateHelmChartErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_installation_failed_error_component import (
            ApiV1KubernetesAppsArchiveCreateInstallationFailedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_installation_running_error_component import (
            ApiV1KubernetesAppsArchiveCreateInstallationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_installed_error_component import (
            ApiV1KubernetesAppsArchiveCreateInstalledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_installed_version_error_component import (
            ApiV1KubernetesAppsArchiveCreateInstalledVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_k8s_cluster_error_component import (
            ApiV1KubernetesAppsArchiveCreateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_kind_error_component import (
            ApiV1KubernetesAppsArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_labels_error_component import (
            ApiV1KubernetesAppsArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_last_installation_error_component import (
            ApiV1KubernetesAppsArchiveCreateLastInstallationErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_last_metrics_check_error_component import (
            ApiV1KubernetesAppsArchiveCreateLastMetricsCheckErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1KubernetesAppsArchiveCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_managed_by_content_type_error_component import (
            ApiV1KubernetesAppsArchiveCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_managed_by_object_id_error_component import (
            ApiV1KubernetesAppsArchiveCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_modified_by_user_error_component import (
            ApiV1KubernetesAppsArchiveCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_name_error_component import (
            ApiV1KubernetesAppsArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_namespace_error_component import (
            ApiV1KubernetesAppsArchiveCreateNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_non_field_errors_error_component import (
            ApiV1KubernetesAppsArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_platform_dns_record_created_error_component import (
            ApiV1KubernetesAppsArchiveCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_platform_service_error_component import (
            ApiV1KubernetesAppsArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_pods_available_error_component import (
            ApiV1KubernetesAppsArchiveCreatePodsAvailableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_pods_details_error_component import (
            ApiV1KubernetesAppsArchiveCreatePodsDetailsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_pods_ready_error_component import (
            ApiV1KubernetesAppsArchiveCreatePodsReadyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_pods_restart_count_last_hour_error_component import (
            ApiV1KubernetesAppsArchiveCreatePodsRestartCountLastHourErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_pods_restart_count_total_error_component import (
            ApiV1KubernetesAppsArchiveCreatePodsRestartCountTotalErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_pods_status_hash_error_component import (
            ApiV1KubernetesAppsArchiveCreatePodsStatusHashErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_pods_status_updated_at_error_component import (
            ApiV1KubernetesAppsArchiveCreatePodsStatusUpdatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_pods_total_error_component import (
            ApiV1KubernetesAppsArchiveCreatePodsTotalErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_pods_unavailable_error_component import (
            ApiV1KubernetesAppsArchiveCreatePodsUnavailableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_provider_error_component import (
            ApiV1KubernetesAppsArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_provider_id_error_component import (
            ApiV1KubernetesAppsArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_provider_reference_error_component import (
            ApiV1KubernetesAppsArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesAppsArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_scope_error_component import (
            ApiV1KubernetesAppsArchiveCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_sla_availability_error_component import (
            ApiV1KubernetesAppsArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_sla_target_error_component import (
            ApiV1KubernetesAppsArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_sla_window_days_error_component import (
            ApiV1KubernetesAppsArchiveCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_slo_availability_error_component import (
            ApiV1KubernetesAppsArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_slo_target_error_component import (
            ApiV1KubernetesAppsArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_slo_window_days_error_component import (
            ApiV1KubernetesAppsArchiveCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_source_error_component import (
            ApiV1KubernetesAppsArchiveCreateSourceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_target_availability_error_component import (
            ApiV1KubernetesAppsArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_uninstallation_failed_error_component import (
            ApiV1KubernetesAppsArchiveCreateUninstallationFailedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_uninstallation_running_error_component import (
            ApiV1KubernetesAppsArchiveCreateUninstallationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_archive_create_uninstalled_error_component import (
            ApiV1KubernetesAppsArchiveCreateUninstalledErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesAppsArchiveCreateActiveErrorComponent
                | ApiV1KubernetesAppsArchiveCreateActualAvailabilityErrorComponent
                | ApiV1KubernetesAppsArchiveCreateAnnotationsErrorComponent
                | ApiV1KubernetesAppsArchiveCreateArchivedAtErrorComponent
                | ApiV1KubernetesAppsArchiveCreateArchivedByErrorComponent
                | ApiV1KubernetesAppsArchiveCreateArchivedErrorComponent
                | ApiV1KubernetesAppsArchiveCreateArchivedReasonErrorComponent
                | ApiV1KubernetesAppsArchiveCreateArtifactErrorComponent
                | ApiV1KubernetesAppsArchiveCreateArtifactPackageErrorComponent
                | ApiV1KubernetesAppsArchiveCreateBlockErrorComponent
                | ApiV1KubernetesAppsArchiveCreateByoaErrorComponent
                | ApiV1KubernetesAppsArchiveCreateCatalogueAppErrorComponent
                | ApiV1KubernetesAppsArchiveCreateCreatedByComponentErrorComponent
                | ApiV1KubernetesAppsArchiveCreateCreatedByUserErrorComponent
                | ApiV1KubernetesAppsArchiveCreateCriticalityErrorComponent
                | ApiV1KubernetesAppsArchiveCreateDebugModeErrorComponent
                | ApiV1KubernetesAppsArchiveCreateDescriptionErrorComponent
                | ApiV1KubernetesAppsArchiveCreateDiscoveryEnabledErrorComponent
                | ApiV1KubernetesAppsArchiveCreateDisplayNameErrorComponent
                | ApiV1KubernetesAppsArchiveCreateExcludedFromDowntimeUntilErrorComponent
                | ApiV1KubernetesAppsArchiveCreateHaEnabledErrorComponent
                | ApiV1KubernetesAppsArchiveCreateHelmChartErrorComponent
                | ApiV1KubernetesAppsArchiveCreateInstallationFailedErrorComponent
                | ApiV1KubernetesAppsArchiveCreateInstallationRunningErrorComponent
                | ApiV1KubernetesAppsArchiveCreateInstalledErrorComponent
                | ApiV1KubernetesAppsArchiveCreateInstalledVersionErrorComponent
                | ApiV1KubernetesAppsArchiveCreateK8SClusterErrorComponent
                | ApiV1KubernetesAppsArchiveCreateKindErrorComponent
                | ApiV1KubernetesAppsArchiveCreateLabelsErrorComponent
                | ApiV1KubernetesAppsArchiveCreateLastInstallationErrorComponent
                | ApiV1KubernetesAppsArchiveCreateLastMetricsCheckErrorComponent
                | ApiV1KubernetesAppsArchiveCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1KubernetesAppsArchiveCreateManagedByContentTypeErrorComponent
                | ApiV1KubernetesAppsArchiveCreateManagedByObjectIdErrorComponent
                | ApiV1KubernetesAppsArchiveCreateModifiedByUserErrorComponent
                | ApiV1KubernetesAppsArchiveCreateNameErrorComponent
                | ApiV1KubernetesAppsArchiveCreateNamespaceErrorComponent
                | ApiV1KubernetesAppsArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1KubernetesAppsArchiveCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1KubernetesAppsArchiveCreatePlatformServiceErrorComponent
                | ApiV1KubernetesAppsArchiveCreatePodsAvailableErrorComponent
                | ApiV1KubernetesAppsArchiveCreatePodsDetailsErrorComponent
                | ApiV1KubernetesAppsArchiveCreatePodsReadyErrorComponent
                | ApiV1KubernetesAppsArchiveCreatePodsRestartCountLastHourErrorComponent
                | ApiV1KubernetesAppsArchiveCreatePodsRestartCountTotalErrorComponent
                | ApiV1KubernetesAppsArchiveCreatePodsStatusHashErrorComponent
                | ApiV1KubernetesAppsArchiveCreatePodsStatusUpdatedAtErrorComponent
                | ApiV1KubernetesAppsArchiveCreatePodsTotalErrorComponent
                | ApiV1KubernetesAppsArchiveCreatePodsUnavailableErrorComponent
                | ApiV1KubernetesAppsArchiveCreateProviderErrorComponent
                | ApiV1KubernetesAppsArchiveCreateProviderIdErrorComponent
                | ApiV1KubernetesAppsArchiveCreateProviderReferenceErrorComponent
                | ApiV1KubernetesAppsArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1KubernetesAppsArchiveCreateScopeErrorComponent
                | ApiV1KubernetesAppsArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1KubernetesAppsArchiveCreateSlaTargetErrorComponent
                | ApiV1KubernetesAppsArchiveCreateSlaWindowDaysErrorComponent
                | ApiV1KubernetesAppsArchiveCreateSloAvailabilityErrorComponent
                | ApiV1KubernetesAppsArchiveCreateSloTargetErrorComponent
                | ApiV1KubernetesAppsArchiveCreateSloWindowDaysErrorComponent
                | ApiV1KubernetesAppsArchiveCreateSourceErrorComponent
                | ApiV1KubernetesAppsArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1KubernetesAppsArchiveCreateUninstallationFailedErrorComponent
                | ApiV1KubernetesAppsArchiveCreateUninstallationRunningErrorComponent
                | ApiV1KubernetesAppsArchiveCreateUninstalledErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_0 = (
                        ApiV1KubernetesAppsArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_1 = (
                        ApiV1KubernetesAppsArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_2 = (
                        ApiV1KubernetesAppsArchiveCreateBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_3 = (
                        ApiV1KubernetesAppsArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_4 = (
                        ApiV1KubernetesAppsArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_5 = (
                        ApiV1KubernetesAppsArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_6 = (
                        ApiV1KubernetesAppsArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_7 = (
                        ApiV1KubernetesAppsArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_8 = (
                        ApiV1KubernetesAppsArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_9 = (
                        ApiV1KubernetesAppsArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_10 = (
                        ApiV1KubernetesAppsArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_11 = (
                        ApiV1KubernetesAppsArchiveCreateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_12 = (
                        ApiV1KubernetesAppsArchiveCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_13 = (
                        ApiV1KubernetesAppsArchiveCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_14 = (
                        ApiV1KubernetesAppsArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_15 = (
                        ApiV1KubernetesAppsArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_16 = (
                        ApiV1KubernetesAppsArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_17 = (
                        ApiV1KubernetesAppsArchiveCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_18 = (
                        ApiV1KubernetesAppsArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_19 = (
                        ApiV1KubernetesAppsArchiveCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_20 = (
                        ApiV1KubernetesAppsArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_21 = (
                        ApiV1KubernetesAppsArchiveCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_22 = (
                        ApiV1KubernetesAppsArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_23 = (
                        ApiV1KubernetesAppsArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_24 = (
                        ApiV1KubernetesAppsArchiveCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_25 = (
                        ApiV1KubernetesAppsArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_26 = (
                        ApiV1KubernetesAppsArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_27 = (
                        ApiV1KubernetesAppsArchiveCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_28 = (
                        ApiV1KubernetesAppsArchiveCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_29 = (
                        ApiV1KubernetesAppsArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_30 = (
                        ApiV1KubernetesAppsArchiveCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_31 = (
                        ApiV1KubernetesAppsArchiveCreateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_32 = (
                        ApiV1KubernetesAppsArchiveCreateSourceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_33 = (
                        ApiV1KubernetesAppsArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_34 = (
                        ApiV1KubernetesAppsArchiveCreateByoaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_35 = (
                        ApiV1KubernetesAppsArchiveCreateNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_36 = (
                        ApiV1KubernetesAppsArchiveCreateHaEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_37 = (
                        ApiV1KubernetesAppsArchiveCreateInstalledVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_38 = (
                        ApiV1KubernetesAppsArchiveCreateInstalledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_39 = (
                        ApiV1KubernetesAppsArchiveCreateUninstalledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_40 = (
                        ApiV1KubernetesAppsArchiveCreateInstallationRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_41 = (
                        ApiV1KubernetesAppsArchiveCreateUninstallationRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_42 = (
                        ApiV1KubernetesAppsArchiveCreateInstallationFailedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_43 = (
                        ApiV1KubernetesAppsArchiveCreateUninstallationFailedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_44 = (
                        ApiV1KubernetesAppsArchiveCreateLastInstallationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_45 = (
                        ApiV1KubernetesAppsArchiveCreateLastMetricsCheckErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_46 = (
                        ApiV1KubernetesAppsArchiveCreatePodsTotalErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_47 = (
                        ApiV1KubernetesAppsArchiveCreatePodsReadyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_48 = (
                        ApiV1KubernetesAppsArchiveCreatePodsAvailableErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_49 = (
                        ApiV1KubernetesAppsArchiveCreatePodsUnavailableErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_50 = (
                        ApiV1KubernetesAppsArchiveCreatePodsRestartCountTotalErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_51 = (
                        ApiV1KubernetesAppsArchiveCreatePodsRestartCountLastHourErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_52 = (
                        ApiV1KubernetesAppsArchiveCreatePodsDetailsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_53 = (
                        ApiV1KubernetesAppsArchiveCreatePodsStatusHashErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_54 = (
                        ApiV1KubernetesAppsArchiveCreatePodsStatusUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_54
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_55 = (
                        ApiV1KubernetesAppsArchiveCreateExcludedFromDowntimeUntilErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_55
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_56 = (
                        ApiV1KubernetesAppsArchiveCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_56
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_57 = (
                        ApiV1KubernetesAppsArchiveCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_57
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_58 = (
                        ApiV1KubernetesAppsArchiveCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_58
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_59 = (
                        ApiV1KubernetesAppsArchiveCreateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_59
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_60 = (
                        ApiV1KubernetesAppsArchiveCreateHelmChartErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_60
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_61 = (
                        ApiV1KubernetesAppsArchiveCreateArtifactPackageErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_61
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_62 = (
                        ApiV1KubernetesAppsArchiveCreateArtifactErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_62
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_63 = (
                        ApiV1KubernetesAppsArchiveCreateCatalogueAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_63
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_64 = (
                    ApiV1KubernetesAppsArchiveCreateK8SClusterErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_apps_archive_create_error_type_64

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_apps_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_apps_archive_create_validation_error.additional_properties = d
        return api_v1_kubernetes_apps_archive_create_validation_error

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
