from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_apps_create_active_error_component import (
        ApiV1KubernetesAppsCreateActiveErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_actual_availability_error_component import (
        ApiV1KubernetesAppsCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_annotations_error_component import (
        ApiV1KubernetesAppsCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_archived_at_error_component import (
        ApiV1KubernetesAppsCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_archived_by_error_component import (
        ApiV1KubernetesAppsCreateArchivedByErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_archived_error_component import (
        ApiV1KubernetesAppsCreateArchivedErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_archived_reason_error_component import (
        ApiV1KubernetesAppsCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_artifact_error_component import (
        ApiV1KubernetesAppsCreateArtifactErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_artifact_package_error_component import (
        ApiV1KubernetesAppsCreateArtifactPackageErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_block_error_component import (
        ApiV1KubernetesAppsCreateBlockErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_byoa_error_component import ApiV1KubernetesAppsCreateByoaErrorComponent
    from ..models.api_v1_kubernetes_apps_create_catalogue_app_error_component import (
        ApiV1KubernetesAppsCreateCatalogueAppErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_created_by_component_error_component import (
        ApiV1KubernetesAppsCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_created_by_user_error_component import (
        ApiV1KubernetesAppsCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_criticality_error_component import (
        ApiV1KubernetesAppsCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_debug_mode_error_component import (
        ApiV1KubernetesAppsCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_description_error_component import (
        ApiV1KubernetesAppsCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_discovery_enabled_error_component import (
        ApiV1KubernetesAppsCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_display_name_error_component import (
        ApiV1KubernetesAppsCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_excluded_from_downtime_until_error_component import (
        ApiV1KubernetesAppsCreateExcludedFromDowntimeUntilErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_ha_enabled_error_component import (
        ApiV1KubernetesAppsCreateHaEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_helm_chart_error_component import (
        ApiV1KubernetesAppsCreateHelmChartErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_installation_failed_error_component import (
        ApiV1KubernetesAppsCreateInstallationFailedErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_installation_running_error_component import (
        ApiV1KubernetesAppsCreateInstallationRunningErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_installed_error_component import (
        ApiV1KubernetesAppsCreateInstalledErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_installed_version_error_component import (
        ApiV1KubernetesAppsCreateInstalledVersionErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_k8s_cluster_error_component import (
        ApiV1KubernetesAppsCreateK8SClusterErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_kind_error_component import ApiV1KubernetesAppsCreateKindErrorComponent
    from ..models.api_v1_kubernetes_apps_create_labels_error_component import (
        ApiV1KubernetesAppsCreateLabelsErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_last_installation_error_component import (
        ApiV1KubernetesAppsCreateLastInstallationErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_last_metrics_check_error_component import (
        ApiV1KubernetesAppsCreateLastMetricsCheckErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1KubernetesAppsCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_managed_by_content_type_error_component import (
        ApiV1KubernetesAppsCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_managed_by_object_id_error_component import (
        ApiV1KubernetesAppsCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_modified_by_user_error_component import (
        ApiV1KubernetesAppsCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_name_error_component import ApiV1KubernetesAppsCreateNameErrorComponent
    from ..models.api_v1_kubernetes_apps_create_namespace_error_component import (
        ApiV1KubernetesAppsCreateNamespaceErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_non_field_errors_error_component import (
        ApiV1KubernetesAppsCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_platform_dns_record_created_error_component import (
        ApiV1KubernetesAppsCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_platform_service_error_component import (
        ApiV1KubernetesAppsCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_pods_available_error_component import (
        ApiV1KubernetesAppsCreatePodsAvailableErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_pods_details_error_component import (
        ApiV1KubernetesAppsCreatePodsDetailsErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_pods_ready_error_component import (
        ApiV1KubernetesAppsCreatePodsReadyErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_pods_restart_count_last_hour_error_component import (
        ApiV1KubernetesAppsCreatePodsRestartCountLastHourErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_pods_restart_count_total_error_component import (
        ApiV1KubernetesAppsCreatePodsRestartCountTotalErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_pods_status_hash_error_component import (
        ApiV1KubernetesAppsCreatePodsStatusHashErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_pods_status_updated_at_error_component import (
        ApiV1KubernetesAppsCreatePodsStatusUpdatedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_pods_total_error_component import (
        ApiV1KubernetesAppsCreatePodsTotalErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_pods_unavailable_error_component import (
        ApiV1KubernetesAppsCreatePodsUnavailableErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_provider_error_component import (
        ApiV1KubernetesAppsCreateProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_provider_id_error_component import (
        ApiV1KubernetesAppsCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_provider_reference_error_component import (
        ApiV1KubernetesAppsCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_reconciliation_enabled_error_component import (
        ApiV1KubernetesAppsCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_scope_error_component import (
        ApiV1KubernetesAppsCreateScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_sla_availability_error_component import (
        ApiV1KubernetesAppsCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_sla_target_error_component import (
        ApiV1KubernetesAppsCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_sla_window_days_error_component import (
        ApiV1KubernetesAppsCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_slo_availability_error_component import (
        ApiV1KubernetesAppsCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_slo_target_error_component import (
        ApiV1KubernetesAppsCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_slo_window_days_error_component import (
        ApiV1KubernetesAppsCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_source_error_component import (
        ApiV1KubernetesAppsCreateSourceErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_target_availability_error_component import (
        ApiV1KubernetesAppsCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_uninstallation_failed_error_component import (
        ApiV1KubernetesAppsCreateUninstallationFailedErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_uninstallation_running_error_component import (
        ApiV1KubernetesAppsCreateUninstallationRunningErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_create_uninstalled_error_component import (
        ApiV1KubernetesAppsCreateUninstalledErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesAppsCreateValidationError")


@_attrs_define
class ApiV1KubernetesAppsCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesAppsCreateActiveErrorComponent |
            ApiV1KubernetesAppsCreateActualAvailabilityErrorComponent | ApiV1KubernetesAppsCreateAnnotationsErrorComponent |
            ApiV1KubernetesAppsCreateArchivedAtErrorComponent | ApiV1KubernetesAppsCreateArchivedByErrorComponent |
            ApiV1KubernetesAppsCreateArchivedErrorComponent | ApiV1KubernetesAppsCreateArchivedReasonErrorComponent |
            ApiV1KubernetesAppsCreateArtifactErrorComponent | ApiV1KubernetesAppsCreateArtifactPackageErrorComponent |
            ApiV1KubernetesAppsCreateBlockErrorComponent | ApiV1KubernetesAppsCreateByoaErrorComponent |
            ApiV1KubernetesAppsCreateCatalogueAppErrorComponent | ApiV1KubernetesAppsCreateCreatedByComponentErrorComponent
            | ApiV1KubernetesAppsCreateCreatedByUserErrorComponent | ApiV1KubernetesAppsCreateCriticalityErrorComponent |
            ApiV1KubernetesAppsCreateDebugModeErrorComponent | ApiV1KubernetesAppsCreateDescriptionErrorComponent |
            ApiV1KubernetesAppsCreateDiscoveryEnabledErrorComponent | ApiV1KubernetesAppsCreateDisplayNameErrorComponent |
            ApiV1KubernetesAppsCreateExcludedFromDowntimeUntilErrorComponent |
            ApiV1KubernetesAppsCreateHaEnabledErrorComponent | ApiV1KubernetesAppsCreateHelmChartErrorComponent |
            ApiV1KubernetesAppsCreateInstallationFailedErrorComponent |
            ApiV1KubernetesAppsCreateInstallationRunningErrorComponent | ApiV1KubernetesAppsCreateInstalledErrorComponent |
            ApiV1KubernetesAppsCreateInstalledVersionErrorComponent | ApiV1KubernetesAppsCreateK8SClusterErrorComponent |
            ApiV1KubernetesAppsCreateKindErrorComponent | ApiV1KubernetesAppsCreateLabelsErrorComponent |
            ApiV1KubernetesAppsCreateLastInstallationErrorComponent |
            ApiV1KubernetesAppsCreateLastMetricsCheckErrorComponent |
            ApiV1KubernetesAppsCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1KubernetesAppsCreateManagedByContentTypeErrorComponent |
            ApiV1KubernetesAppsCreateManagedByObjectIdErrorComponent | ApiV1KubernetesAppsCreateModifiedByUserErrorComponent
            | ApiV1KubernetesAppsCreateNameErrorComponent | ApiV1KubernetesAppsCreateNamespaceErrorComponent |
            ApiV1KubernetesAppsCreateNonFieldErrorsErrorComponent |
            ApiV1KubernetesAppsCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1KubernetesAppsCreatePlatformServiceErrorComponent | ApiV1KubernetesAppsCreatePodsAvailableErrorComponent |
            ApiV1KubernetesAppsCreatePodsDetailsErrorComponent | ApiV1KubernetesAppsCreatePodsReadyErrorComponent |
            ApiV1KubernetesAppsCreatePodsRestartCountLastHourErrorComponent |
            ApiV1KubernetesAppsCreatePodsRestartCountTotalErrorComponent |
            ApiV1KubernetesAppsCreatePodsStatusHashErrorComponent |
            ApiV1KubernetesAppsCreatePodsStatusUpdatedAtErrorComponent | ApiV1KubernetesAppsCreatePodsTotalErrorComponent |
            ApiV1KubernetesAppsCreatePodsUnavailableErrorComponent | ApiV1KubernetesAppsCreateProviderErrorComponent |
            ApiV1KubernetesAppsCreateProviderIdErrorComponent | ApiV1KubernetesAppsCreateProviderReferenceErrorComponent |
            ApiV1KubernetesAppsCreateReconciliationEnabledErrorComponent | ApiV1KubernetesAppsCreateScopeErrorComponent |
            ApiV1KubernetesAppsCreateSlaAvailabilityErrorComponent | ApiV1KubernetesAppsCreateSlaTargetErrorComponent |
            ApiV1KubernetesAppsCreateSlaWindowDaysErrorComponent | ApiV1KubernetesAppsCreateSloAvailabilityErrorComponent |
            ApiV1KubernetesAppsCreateSloTargetErrorComponent | ApiV1KubernetesAppsCreateSloWindowDaysErrorComponent |
            ApiV1KubernetesAppsCreateSourceErrorComponent | ApiV1KubernetesAppsCreateTargetAvailabilityErrorComponent |
            ApiV1KubernetesAppsCreateUninstallationFailedErrorComponent |
            ApiV1KubernetesAppsCreateUninstallationRunningErrorComponent |
            ApiV1KubernetesAppsCreateUninstalledErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesAppsCreateActiveErrorComponent
        | ApiV1KubernetesAppsCreateActualAvailabilityErrorComponent
        | ApiV1KubernetesAppsCreateAnnotationsErrorComponent
        | ApiV1KubernetesAppsCreateArchivedAtErrorComponent
        | ApiV1KubernetesAppsCreateArchivedByErrorComponent
        | ApiV1KubernetesAppsCreateArchivedErrorComponent
        | ApiV1KubernetesAppsCreateArchivedReasonErrorComponent
        | ApiV1KubernetesAppsCreateArtifactErrorComponent
        | ApiV1KubernetesAppsCreateArtifactPackageErrorComponent
        | ApiV1KubernetesAppsCreateBlockErrorComponent
        | ApiV1KubernetesAppsCreateByoaErrorComponent
        | ApiV1KubernetesAppsCreateCatalogueAppErrorComponent
        | ApiV1KubernetesAppsCreateCreatedByComponentErrorComponent
        | ApiV1KubernetesAppsCreateCreatedByUserErrorComponent
        | ApiV1KubernetesAppsCreateCriticalityErrorComponent
        | ApiV1KubernetesAppsCreateDebugModeErrorComponent
        | ApiV1KubernetesAppsCreateDescriptionErrorComponent
        | ApiV1KubernetesAppsCreateDiscoveryEnabledErrorComponent
        | ApiV1KubernetesAppsCreateDisplayNameErrorComponent
        | ApiV1KubernetesAppsCreateExcludedFromDowntimeUntilErrorComponent
        | ApiV1KubernetesAppsCreateHaEnabledErrorComponent
        | ApiV1KubernetesAppsCreateHelmChartErrorComponent
        | ApiV1KubernetesAppsCreateInstallationFailedErrorComponent
        | ApiV1KubernetesAppsCreateInstallationRunningErrorComponent
        | ApiV1KubernetesAppsCreateInstalledErrorComponent
        | ApiV1KubernetesAppsCreateInstalledVersionErrorComponent
        | ApiV1KubernetesAppsCreateK8SClusterErrorComponent
        | ApiV1KubernetesAppsCreateKindErrorComponent
        | ApiV1KubernetesAppsCreateLabelsErrorComponent
        | ApiV1KubernetesAppsCreateLastInstallationErrorComponent
        | ApiV1KubernetesAppsCreateLastMetricsCheckErrorComponent
        | ApiV1KubernetesAppsCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1KubernetesAppsCreateManagedByContentTypeErrorComponent
        | ApiV1KubernetesAppsCreateManagedByObjectIdErrorComponent
        | ApiV1KubernetesAppsCreateModifiedByUserErrorComponent
        | ApiV1KubernetesAppsCreateNameErrorComponent
        | ApiV1KubernetesAppsCreateNamespaceErrorComponent
        | ApiV1KubernetesAppsCreateNonFieldErrorsErrorComponent
        | ApiV1KubernetesAppsCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1KubernetesAppsCreatePlatformServiceErrorComponent
        | ApiV1KubernetesAppsCreatePodsAvailableErrorComponent
        | ApiV1KubernetesAppsCreatePodsDetailsErrorComponent
        | ApiV1KubernetesAppsCreatePodsReadyErrorComponent
        | ApiV1KubernetesAppsCreatePodsRestartCountLastHourErrorComponent
        | ApiV1KubernetesAppsCreatePodsRestartCountTotalErrorComponent
        | ApiV1KubernetesAppsCreatePodsStatusHashErrorComponent
        | ApiV1KubernetesAppsCreatePodsStatusUpdatedAtErrorComponent
        | ApiV1KubernetesAppsCreatePodsTotalErrorComponent
        | ApiV1KubernetesAppsCreatePodsUnavailableErrorComponent
        | ApiV1KubernetesAppsCreateProviderErrorComponent
        | ApiV1KubernetesAppsCreateProviderIdErrorComponent
        | ApiV1KubernetesAppsCreateProviderReferenceErrorComponent
        | ApiV1KubernetesAppsCreateReconciliationEnabledErrorComponent
        | ApiV1KubernetesAppsCreateScopeErrorComponent
        | ApiV1KubernetesAppsCreateSlaAvailabilityErrorComponent
        | ApiV1KubernetesAppsCreateSlaTargetErrorComponent
        | ApiV1KubernetesAppsCreateSlaWindowDaysErrorComponent
        | ApiV1KubernetesAppsCreateSloAvailabilityErrorComponent
        | ApiV1KubernetesAppsCreateSloTargetErrorComponent
        | ApiV1KubernetesAppsCreateSloWindowDaysErrorComponent
        | ApiV1KubernetesAppsCreateSourceErrorComponent
        | ApiV1KubernetesAppsCreateTargetAvailabilityErrorComponent
        | ApiV1KubernetesAppsCreateUninstallationFailedErrorComponent
        | ApiV1KubernetesAppsCreateUninstallationRunningErrorComponent
        | ApiV1KubernetesAppsCreateUninstalledErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_apps_create_active_error_component import (
            ApiV1KubernetesAppsCreateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_actual_availability_error_component import (
            ApiV1KubernetesAppsCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_annotations_error_component import (
            ApiV1KubernetesAppsCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_archived_at_error_component import (
            ApiV1KubernetesAppsCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_archived_by_error_component import (
            ApiV1KubernetesAppsCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_archived_error_component import (
            ApiV1KubernetesAppsCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_archived_reason_error_component import (
            ApiV1KubernetesAppsCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_artifact_error_component import (
            ApiV1KubernetesAppsCreateArtifactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_artifact_package_error_component import (
            ApiV1KubernetesAppsCreateArtifactPackageErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_block_error_component import (
            ApiV1KubernetesAppsCreateBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_byoa_error_component import (
            ApiV1KubernetesAppsCreateByoaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_catalogue_app_error_component import (
            ApiV1KubernetesAppsCreateCatalogueAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_created_by_component_error_component import (
            ApiV1KubernetesAppsCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_created_by_user_error_component import (
            ApiV1KubernetesAppsCreateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_criticality_error_component import (
            ApiV1KubernetesAppsCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_debug_mode_error_component import (
            ApiV1KubernetesAppsCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_description_error_component import (
            ApiV1KubernetesAppsCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_discovery_enabled_error_component import (
            ApiV1KubernetesAppsCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_display_name_error_component import (
            ApiV1KubernetesAppsCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_excluded_from_downtime_until_error_component import (
            ApiV1KubernetesAppsCreateExcludedFromDowntimeUntilErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_ha_enabled_error_component import (
            ApiV1KubernetesAppsCreateHaEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_helm_chart_error_component import (
            ApiV1KubernetesAppsCreateHelmChartErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_installation_failed_error_component import (
            ApiV1KubernetesAppsCreateInstallationFailedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_installation_running_error_component import (
            ApiV1KubernetesAppsCreateInstallationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_installed_error_component import (
            ApiV1KubernetesAppsCreateInstalledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_installed_version_error_component import (
            ApiV1KubernetesAppsCreateInstalledVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_kind_error_component import (
            ApiV1KubernetesAppsCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_labels_error_component import (
            ApiV1KubernetesAppsCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_last_installation_error_component import (
            ApiV1KubernetesAppsCreateLastInstallationErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_last_metrics_check_error_component import (
            ApiV1KubernetesAppsCreateLastMetricsCheckErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1KubernetesAppsCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_managed_by_content_type_error_component import (
            ApiV1KubernetesAppsCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_managed_by_object_id_error_component import (
            ApiV1KubernetesAppsCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_modified_by_user_error_component import (
            ApiV1KubernetesAppsCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_name_error_component import (
            ApiV1KubernetesAppsCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_namespace_error_component import (
            ApiV1KubernetesAppsCreateNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_non_field_errors_error_component import (
            ApiV1KubernetesAppsCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_platform_dns_record_created_error_component import (
            ApiV1KubernetesAppsCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_platform_service_error_component import (
            ApiV1KubernetesAppsCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_pods_available_error_component import (
            ApiV1KubernetesAppsCreatePodsAvailableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_pods_details_error_component import (
            ApiV1KubernetesAppsCreatePodsDetailsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_pods_ready_error_component import (
            ApiV1KubernetesAppsCreatePodsReadyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_pods_restart_count_last_hour_error_component import (
            ApiV1KubernetesAppsCreatePodsRestartCountLastHourErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_pods_restart_count_total_error_component import (
            ApiV1KubernetesAppsCreatePodsRestartCountTotalErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_pods_status_hash_error_component import (
            ApiV1KubernetesAppsCreatePodsStatusHashErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_pods_status_updated_at_error_component import (
            ApiV1KubernetesAppsCreatePodsStatusUpdatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_pods_total_error_component import (
            ApiV1KubernetesAppsCreatePodsTotalErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_pods_unavailable_error_component import (
            ApiV1KubernetesAppsCreatePodsUnavailableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_provider_error_component import (
            ApiV1KubernetesAppsCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_provider_id_error_component import (
            ApiV1KubernetesAppsCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_provider_reference_error_component import (
            ApiV1KubernetesAppsCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesAppsCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_scope_error_component import (
            ApiV1KubernetesAppsCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_sla_availability_error_component import (
            ApiV1KubernetesAppsCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_sla_target_error_component import (
            ApiV1KubernetesAppsCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_sla_window_days_error_component import (
            ApiV1KubernetesAppsCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_slo_availability_error_component import (
            ApiV1KubernetesAppsCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_slo_target_error_component import (
            ApiV1KubernetesAppsCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_slo_window_days_error_component import (
            ApiV1KubernetesAppsCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_source_error_component import (
            ApiV1KubernetesAppsCreateSourceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_target_availability_error_component import (
            ApiV1KubernetesAppsCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_uninstallation_failed_error_component import (
            ApiV1KubernetesAppsCreateUninstallationFailedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_uninstallation_running_error_component import (
            ApiV1KubernetesAppsCreateUninstallationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_uninstalled_error_component import (
            ApiV1KubernetesAppsCreateUninstalledErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesAppsCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateLastReconciliationDurationSecondsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateSourceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateByoaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateNamespaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateHaEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateInstalledVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateInstalledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateUninstalledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateInstallationRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateUninstallationRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateInstallationFailedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateUninstallationFailedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateLastInstallationErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateLastMetricsCheckErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreatePodsTotalErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreatePodsReadyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreatePodsAvailableErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreatePodsUnavailableErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreatePodsRestartCountTotalErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreatePodsRestartCountLastHourErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreatePodsDetailsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreatePodsStatusHashErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreatePodsStatusUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateExcludedFromDowntimeUntilErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateCreatedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateHelmChartErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateArtifactPackageErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateArtifactErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsCreateCatalogueAppErrorComponent):
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
        from ..models.api_v1_kubernetes_apps_create_active_error_component import (
            ApiV1KubernetesAppsCreateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_actual_availability_error_component import (
            ApiV1KubernetesAppsCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_annotations_error_component import (
            ApiV1KubernetesAppsCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_archived_at_error_component import (
            ApiV1KubernetesAppsCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_archived_by_error_component import (
            ApiV1KubernetesAppsCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_archived_error_component import (
            ApiV1KubernetesAppsCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_archived_reason_error_component import (
            ApiV1KubernetesAppsCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_artifact_error_component import (
            ApiV1KubernetesAppsCreateArtifactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_artifact_package_error_component import (
            ApiV1KubernetesAppsCreateArtifactPackageErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_block_error_component import (
            ApiV1KubernetesAppsCreateBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_byoa_error_component import (
            ApiV1KubernetesAppsCreateByoaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_catalogue_app_error_component import (
            ApiV1KubernetesAppsCreateCatalogueAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_created_by_component_error_component import (
            ApiV1KubernetesAppsCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_created_by_user_error_component import (
            ApiV1KubernetesAppsCreateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_criticality_error_component import (
            ApiV1KubernetesAppsCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_debug_mode_error_component import (
            ApiV1KubernetesAppsCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_description_error_component import (
            ApiV1KubernetesAppsCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_discovery_enabled_error_component import (
            ApiV1KubernetesAppsCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_display_name_error_component import (
            ApiV1KubernetesAppsCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_excluded_from_downtime_until_error_component import (
            ApiV1KubernetesAppsCreateExcludedFromDowntimeUntilErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_ha_enabled_error_component import (
            ApiV1KubernetesAppsCreateHaEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_helm_chart_error_component import (
            ApiV1KubernetesAppsCreateHelmChartErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_installation_failed_error_component import (
            ApiV1KubernetesAppsCreateInstallationFailedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_installation_running_error_component import (
            ApiV1KubernetesAppsCreateInstallationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_installed_error_component import (
            ApiV1KubernetesAppsCreateInstalledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_installed_version_error_component import (
            ApiV1KubernetesAppsCreateInstalledVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_k8s_cluster_error_component import (
            ApiV1KubernetesAppsCreateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_kind_error_component import (
            ApiV1KubernetesAppsCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_labels_error_component import (
            ApiV1KubernetesAppsCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_last_installation_error_component import (
            ApiV1KubernetesAppsCreateLastInstallationErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_last_metrics_check_error_component import (
            ApiV1KubernetesAppsCreateLastMetricsCheckErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1KubernetesAppsCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_managed_by_content_type_error_component import (
            ApiV1KubernetesAppsCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_managed_by_object_id_error_component import (
            ApiV1KubernetesAppsCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_modified_by_user_error_component import (
            ApiV1KubernetesAppsCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_name_error_component import (
            ApiV1KubernetesAppsCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_namespace_error_component import (
            ApiV1KubernetesAppsCreateNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_non_field_errors_error_component import (
            ApiV1KubernetesAppsCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_platform_dns_record_created_error_component import (
            ApiV1KubernetesAppsCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_platform_service_error_component import (
            ApiV1KubernetesAppsCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_pods_available_error_component import (
            ApiV1KubernetesAppsCreatePodsAvailableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_pods_details_error_component import (
            ApiV1KubernetesAppsCreatePodsDetailsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_pods_ready_error_component import (
            ApiV1KubernetesAppsCreatePodsReadyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_pods_restart_count_last_hour_error_component import (
            ApiV1KubernetesAppsCreatePodsRestartCountLastHourErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_pods_restart_count_total_error_component import (
            ApiV1KubernetesAppsCreatePodsRestartCountTotalErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_pods_status_hash_error_component import (
            ApiV1KubernetesAppsCreatePodsStatusHashErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_pods_status_updated_at_error_component import (
            ApiV1KubernetesAppsCreatePodsStatusUpdatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_pods_total_error_component import (
            ApiV1KubernetesAppsCreatePodsTotalErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_pods_unavailable_error_component import (
            ApiV1KubernetesAppsCreatePodsUnavailableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_provider_error_component import (
            ApiV1KubernetesAppsCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_provider_id_error_component import (
            ApiV1KubernetesAppsCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_provider_reference_error_component import (
            ApiV1KubernetesAppsCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesAppsCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_scope_error_component import (
            ApiV1KubernetesAppsCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_sla_availability_error_component import (
            ApiV1KubernetesAppsCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_sla_target_error_component import (
            ApiV1KubernetesAppsCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_sla_window_days_error_component import (
            ApiV1KubernetesAppsCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_slo_availability_error_component import (
            ApiV1KubernetesAppsCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_slo_target_error_component import (
            ApiV1KubernetesAppsCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_slo_window_days_error_component import (
            ApiV1KubernetesAppsCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_source_error_component import (
            ApiV1KubernetesAppsCreateSourceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_target_availability_error_component import (
            ApiV1KubernetesAppsCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_uninstallation_failed_error_component import (
            ApiV1KubernetesAppsCreateUninstallationFailedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_uninstallation_running_error_component import (
            ApiV1KubernetesAppsCreateUninstallationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_create_uninstalled_error_component import (
            ApiV1KubernetesAppsCreateUninstalledErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesAppsCreateActiveErrorComponent
                | ApiV1KubernetesAppsCreateActualAvailabilityErrorComponent
                | ApiV1KubernetesAppsCreateAnnotationsErrorComponent
                | ApiV1KubernetesAppsCreateArchivedAtErrorComponent
                | ApiV1KubernetesAppsCreateArchivedByErrorComponent
                | ApiV1KubernetesAppsCreateArchivedErrorComponent
                | ApiV1KubernetesAppsCreateArchivedReasonErrorComponent
                | ApiV1KubernetesAppsCreateArtifactErrorComponent
                | ApiV1KubernetesAppsCreateArtifactPackageErrorComponent
                | ApiV1KubernetesAppsCreateBlockErrorComponent
                | ApiV1KubernetesAppsCreateByoaErrorComponent
                | ApiV1KubernetesAppsCreateCatalogueAppErrorComponent
                | ApiV1KubernetesAppsCreateCreatedByComponentErrorComponent
                | ApiV1KubernetesAppsCreateCreatedByUserErrorComponent
                | ApiV1KubernetesAppsCreateCriticalityErrorComponent
                | ApiV1KubernetesAppsCreateDebugModeErrorComponent
                | ApiV1KubernetesAppsCreateDescriptionErrorComponent
                | ApiV1KubernetesAppsCreateDiscoveryEnabledErrorComponent
                | ApiV1KubernetesAppsCreateDisplayNameErrorComponent
                | ApiV1KubernetesAppsCreateExcludedFromDowntimeUntilErrorComponent
                | ApiV1KubernetesAppsCreateHaEnabledErrorComponent
                | ApiV1KubernetesAppsCreateHelmChartErrorComponent
                | ApiV1KubernetesAppsCreateInstallationFailedErrorComponent
                | ApiV1KubernetesAppsCreateInstallationRunningErrorComponent
                | ApiV1KubernetesAppsCreateInstalledErrorComponent
                | ApiV1KubernetesAppsCreateInstalledVersionErrorComponent
                | ApiV1KubernetesAppsCreateK8SClusterErrorComponent
                | ApiV1KubernetesAppsCreateKindErrorComponent
                | ApiV1KubernetesAppsCreateLabelsErrorComponent
                | ApiV1KubernetesAppsCreateLastInstallationErrorComponent
                | ApiV1KubernetesAppsCreateLastMetricsCheckErrorComponent
                | ApiV1KubernetesAppsCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1KubernetesAppsCreateManagedByContentTypeErrorComponent
                | ApiV1KubernetesAppsCreateManagedByObjectIdErrorComponent
                | ApiV1KubernetesAppsCreateModifiedByUserErrorComponent
                | ApiV1KubernetesAppsCreateNameErrorComponent
                | ApiV1KubernetesAppsCreateNamespaceErrorComponent
                | ApiV1KubernetesAppsCreateNonFieldErrorsErrorComponent
                | ApiV1KubernetesAppsCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1KubernetesAppsCreatePlatformServiceErrorComponent
                | ApiV1KubernetesAppsCreatePodsAvailableErrorComponent
                | ApiV1KubernetesAppsCreatePodsDetailsErrorComponent
                | ApiV1KubernetesAppsCreatePodsReadyErrorComponent
                | ApiV1KubernetesAppsCreatePodsRestartCountLastHourErrorComponent
                | ApiV1KubernetesAppsCreatePodsRestartCountTotalErrorComponent
                | ApiV1KubernetesAppsCreatePodsStatusHashErrorComponent
                | ApiV1KubernetesAppsCreatePodsStatusUpdatedAtErrorComponent
                | ApiV1KubernetesAppsCreatePodsTotalErrorComponent
                | ApiV1KubernetesAppsCreatePodsUnavailableErrorComponent
                | ApiV1KubernetesAppsCreateProviderErrorComponent
                | ApiV1KubernetesAppsCreateProviderIdErrorComponent
                | ApiV1KubernetesAppsCreateProviderReferenceErrorComponent
                | ApiV1KubernetesAppsCreateReconciliationEnabledErrorComponent
                | ApiV1KubernetesAppsCreateScopeErrorComponent
                | ApiV1KubernetesAppsCreateSlaAvailabilityErrorComponent
                | ApiV1KubernetesAppsCreateSlaTargetErrorComponent
                | ApiV1KubernetesAppsCreateSlaWindowDaysErrorComponent
                | ApiV1KubernetesAppsCreateSloAvailabilityErrorComponent
                | ApiV1KubernetesAppsCreateSloTargetErrorComponent
                | ApiV1KubernetesAppsCreateSloWindowDaysErrorComponent
                | ApiV1KubernetesAppsCreateSourceErrorComponent
                | ApiV1KubernetesAppsCreateTargetAvailabilityErrorComponent
                | ApiV1KubernetesAppsCreateUninstallationFailedErrorComponent
                | ApiV1KubernetesAppsCreateUninstallationRunningErrorComponent
                | ApiV1KubernetesAppsCreateUninstalledErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_0 = (
                        ApiV1KubernetesAppsCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_1 = (
                        ApiV1KubernetesAppsCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_2 = (
                        ApiV1KubernetesAppsCreateBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_3 = (
                        ApiV1KubernetesAppsCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_4 = (
                        ApiV1KubernetesAppsCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_5 = (
                        ApiV1KubernetesAppsCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_6 = (
                        ApiV1KubernetesAppsCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_7 = (
                        ApiV1KubernetesAppsCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_8 = (
                        ApiV1KubernetesAppsCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_9 = (
                        ApiV1KubernetesAppsCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_10 = (
                        ApiV1KubernetesAppsCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_11 = (
                        ApiV1KubernetesAppsCreateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_12 = (
                        ApiV1KubernetesAppsCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_13 = (
                        ApiV1KubernetesAppsCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_14 = (
                        ApiV1KubernetesAppsCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_15 = (
                        ApiV1KubernetesAppsCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_16 = (
                        ApiV1KubernetesAppsCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_17 = (
                        ApiV1KubernetesAppsCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_18 = (
                        ApiV1KubernetesAppsCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_19 = (
                        ApiV1KubernetesAppsCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_20 = (
                        ApiV1KubernetesAppsCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_21 = (
                        ApiV1KubernetesAppsCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_22 = (
                        ApiV1KubernetesAppsCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_23 = (
                        ApiV1KubernetesAppsCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_24 = (
                        ApiV1KubernetesAppsCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_25 = (
                        ApiV1KubernetesAppsCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_26 = (
                        ApiV1KubernetesAppsCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_27 = (
                        ApiV1KubernetesAppsCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_28 = (
                        ApiV1KubernetesAppsCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_29 = (
                        ApiV1KubernetesAppsCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_30 = (
                        ApiV1KubernetesAppsCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_31 = (
                        ApiV1KubernetesAppsCreateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_32 = (
                        ApiV1KubernetesAppsCreateSourceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_33 = (
                        ApiV1KubernetesAppsCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_34 = (
                        ApiV1KubernetesAppsCreateByoaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_35 = (
                        ApiV1KubernetesAppsCreateNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_36 = (
                        ApiV1KubernetesAppsCreateHaEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_37 = (
                        ApiV1KubernetesAppsCreateInstalledVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_38 = (
                        ApiV1KubernetesAppsCreateInstalledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_39 = (
                        ApiV1KubernetesAppsCreateUninstalledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_40 = (
                        ApiV1KubernetesAppsCreateInstallationRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_41 = (
                        ApiV1KubernetesAppsCreateUninstallationRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_42 = (
                        ApiV1KubernetesAppsCreateInstallationFailedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_43 = (
                        ApiV1KubernetesAppsCreateUninstallationFailedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_44 = (
                        ApiV1KubernetesAppsCreateLastInstallationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_45 = (
                        ApiV1KubernetesAppsCreateLastMetricsCheckErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_46 = (
                        ApiV1KubernetesAppsCreatePodsTotalErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_47 = (
                        ApiV1KubernetesAppsCreatePodsReadyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_48 = (
                        ApiV1KubernetesAppsCreatePodsAvailableErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_49 = (
                        ApiV1KubernetesAppsCreatePodsUnavailableErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_50 = (
                        ApiV1KubernetesAppsCreatePodsRestartCountTotalErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_51 = (
                        ApiV1KubernetesAppsCreatePodsRestartCountLastHourErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_52 = (
                        ApiV1KubernetesAppsCreatePodsDetailsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_53 = (
                        ApiV1KubernetesAppsCreatePodsStatusHashErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_54 = (
                        ApiV1KubernetesAppsCreatePodsStatusUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_54
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_55 = (
                        ApiV1KubernetesAppsCreateExcludedFromDowntimeUntilErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_55
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_56 = (
                        ApiV1KubernetesAppsCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_56
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_57 = (
                        ApiV1KubernetesAppsCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_57
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_58 = (
                        ApiV1KubernetesAppsCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_58
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_59 = (
                        ApiV1KubernetesAppsCreateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_59
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_60 = (
                        ApiV1KubernetesAppsCreateHelmChartErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_60
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_61 = (
                        ApiV1KubernetesAppsCreateArtifactPackageErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_61
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_62 = (
                        ApiV1KubernetesAppsCreateArtifactErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_62
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_create_error_type_63 = (
                        ApiV1KubernetesAppsCreateCatalogueAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_create_error_type_63
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_apps_create_error_type_64 = (
                    ApiV1KubernetesAppsCreateK8SClusterErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_apps_create_error_type_64

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_apps_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_apps_create_validation_error.additional_properties = d
        return api_v1_kubernetes_apps_create_validation_error

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
