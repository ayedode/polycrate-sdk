from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_workspaces_reconcile_create_actual_availability_error_component import (
        ApiV1WorkspacesReconcileCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_alternative_name_error_component import (
        ApiV1WorkspacesReconcileCreateAlternativeNameErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_annotations_error_component import (
        ApiV1WorkspacesReconcileCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_archived_at_error_component import (
        ApiV1WorkspacesReconcileCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_archived_error_component import (
        ApiV1WorkspacesReconcileCreateArchivedErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_archived_reason_error_component import (
        ApiV1WorkspacesReconcileCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_backup_enabled_error_component import (
        ApiV1WorkspacesReconcileCreateBackupEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_criticality_error_component import (
        ApiV1WorkspacesReconcileCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_debug_mode_error_component import (
        ApiV1WorkspacesReconcileCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_description_error_component import (
        ApiV1WorkspacesReconcileCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_discovery_enabled_error_component import (
        ApiV1WorkspacesReconcileCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_display_name_error_component import (
        ApiV1WorkspacesReconcileCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_encrypted_error_component import (
        ApiV1WorkspacesReconcileCreateEncryptedErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_endpoint_monitoring_mode_error_component import (
        ApiV1WorkspacesReconcileCreateEndpointMonitoringModeErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_endpoint_monitors_error_component import (
        ApiV1WorkspacesReconcileCreateEndpointMonitorsErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_gitlab_project_id_error_component import (
        ApiV1WorkspacesReconcileCreateGitlabProjectIdErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_gitlab_project_url_error_component import (
        ApiV1WorkspacesReconcileCreateGitlabProjectUrlErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_global_endpoint_monitor_error_component import (
        ApiV1WorkspacesReconcileCreateGlobalEndpointMonitorErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_has_incompatible_kubeconfig_error_component import (
        ApiV1WorkspacesReconcileCreateHasIncompatibleKubeconfigErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_k8s_addons_enabled_error_component import (
        ApiV1WorkspacesReconcileCreateK8SAddonsEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_kind_error_component import (
        ApiV1WorkspacesReconcileCreateKindErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_labels_error_component import (
        ApiV1WorkspacesReconcileCreateLabelsErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_logs_enabled_error_component import (
        ApiV1WorkspacesReconcileCreateLogsEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_metrics_enabled_error_component import (
        ApiV1WorkspacesReconcileCreateMetricsEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_monitoring_workspace_allowlist_ids_error_component import (
        ApiV1WorkspacesReconcileCreateMonitoringWorkspaceAllowlistIdsErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_name_error_component import (
        ApiV1WorkspacesReconcileCreateNameErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_non_field_errors_error_component import (
        ApiV1WorkspacesReconcileCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_notifications_enabled_error_component import (
        ApiV1WorkspacesReconcileCreateNotificationsEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_on_premise_error_component import (
        ApiV1WorkspacesReconcileCreateOnPremiseErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_organization_id_error_component import (
        ApiV1WorkspacesReconcileCreateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_owner_id_error_component import (
        ApiV1WorkspacesReconcileCreateOwnerIdErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_platform_service_error_component import (
        ApiV1WorkspacesReconcileCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_pop_id_error_component import (
        ApiV1WorkspacesReconcileCreatePopIdErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_provider_error_component import (
        ApiV1WorkspacesReconcileCreateProviderErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_provider_id_error_component import (
        ApiV1WorkspacesReconcileCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_provider_reference_error_component import (
        ApiV1WorkspacesReconcileCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_purpose_error_component import (
        ApiV1WorkspacesReconcileCreatePurposeErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_readme_md_error_component import (
        ApiV1WorkspacesReconcileCreateReadmeMdErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_reconciliation_enabled_error_component import (
        ApiV1WorkspacesReconcileCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_scope_error_component import (
        ApiV1WorkspacesReconcileCreateScopeErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_secrets_poly_raw_error_component import (
        ApiV1WorkspacesReconcileCreateSecretsPolyRawErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_sla_availability_error_component import (
        ApiV1WorkspacesReconcileCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_sla_target_error_component import (
        ApiV1WorkspacesReconcileCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_slo_availability_error_component import (
        ApiV1WorkspacesReconcileCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_slo_target_error_component import (
        ApiV1WorkspacesReconcileCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_target_availability_error_component import (
        ApiV1WorkspacesReconcileCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_template_error_component import (
        ApiV1WorkspacesReconcileCreateTemplateErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_urls_error_component import (
        ApiV1WorkspacesReconcileCreateUrlsErrorComponent,
    )
    from ..models.api_v1_workspaces_reconcile_create_workspace_inventory_raw_error_component import (
        ApiV1WorkspacesReconcileCreateWorkspaceInventoryRawErrorComponent,
    )


T = TypeVar("T", bound="ApiV1WorkspacesReconcileCreateValidationError")


@_attrs_define
class ApiV1WorkspacesReconcileCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1WorkspacesReconcileCreateActualAvailabilityErrorComponent |
            ApiV1WorkspacesReconcileCreateAlternativeNameErrorComponent |
            ApiV1WorkspacesReconcileCreateAnnotationsErrorComponent | ApiV1WorkspacesReconcileCreateArchivedAtErrorComponent
            | ApiV1WorkspacesReconcileCreateArchivedErrorComponent |
            ApiV1WorkspacesReconcileCreateArchivedReasonErrorComponent |
            ApiV1WorkspacesReconcileCreateBackupEnabledErrorComponent |
            ApiV1WorkspacesReconcileCreateCriticalityErrorComponent | ApiV1WorkspacesReconcileCreateDebugModeErrorComponent
            | ApiV1WorkspacesReconcileCreateDescriptionErrorComponent |
            ApiV1WorkspacesReconcileCreateDiscoveryEnabledErrorComponent |
            ApiV1WorkspacesReconcileCreateDisplayNameErrorComponent | ApiV1WorkspacesReconcileCreateEncryptedErrorComponent
            | ApiV1WorkspacesReconcileCreateEndpointMonitoringModeErrorComponent |
            ApiV1WorkspacesReconcileCreateEndpointMonitorsErrorComponent |
            ApiV1WorkspacesReconcileCreateGitlabProjectIdErrorComponent |
            ApiV1WorkspacesReconcileCreateGitlabProjectUrlErrorComponent |
            ApiV1WorkspacesReconcileCreateGlobalEndpointMonitorErrorComponent |
            ApiV1WorkspacesReconcileCreateHasIncompatibleKubeconfigErrorComponent |
            ApiV1WorkspacesReconcileCreateK8SAddonsEnabledErrorComponent | ApiV1WorkspacesReconcileCreateKindErrorComponent
            | ApiV1WorkspacesReconcileCreateLabelsErrorComponent | ApiV1WorkspacesReconcileCreateLogsEnabledErrorComponent |
            ApiV1WorkspacesReconcileCreateMetricsEnabledErrorComponent |
            ApiV1WorkspacesReconcileCreateMonitoringWorkspaceAllowlistIdsErrorComponent |
            ApiV1WorkspacesReconcileCreateNameErrorComponent | ApiV1WorkspacesReconcileCreateNonFieldErrorsErrorComponent |
            ApiV1WorkspacesReconcileCreateNotificationsEnabledErrorComponent |
            ApiV1WorkspacesReconcileCreateOnPremiseErrorComponent |
            ApiV1WorkspacesReconcileCreateOrganizationIdErrorComponent | ApiV1WorkspacesReconcileCreateOwnerIdErrorComponent
            | ApiV1WorkspacesReconcileCreatePlatformServiceErrorComponent |
            ApiV1WorkspacesReconcileCreatePopIdErrorComponent | ApiV1WorkspacesReconcileCreateProviderErrorComponent |
            ApiV1WorkspacesReconcileCreateProviderIdErrorComponent |
            ApiV1WorkspacesReconcileCreateProviderReferenceErrorComponent |
            ApiV1WorkspacesReconcileCreatePurposeErrorComponent | ApiV1WorkspacesReconcileCreateReadmeMdErrorComponent |
            ApiV1WorkspacesReconcileCreateReconciliationEnabledErrorComponent |
            ApiV1WorkspacesReconcileCreateScopeErrorComponent | ApiV1WorkspacesReconcileCreateSecretsPolyRawErrorComponent |
            ApiV1WorkspacesReconcileCreateSlaAvailabilityErrorComponent |
            ApiV1WorkspacesReconcileCreateSlaTargetErrorComponent |
            ApiV1WorkspacesReconcileCreateSloAvailabilityErrorComponent |
            ApiV1WorkspacesReconcileCreateSloTargetErrorComponent |
            ApiV1WorkspacesReconcileCreateTargetAvailabilityErrorComponent |
            ApiV1WorkspacesReconcileCreateTemplateErrorComponent | ApiV1WorkspacesReconcileCreateUrlsErrorComponent |
            ApiV1WorkspacesReconcileCreateWorkspaceInventoryRawErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1WorkspacesReconcileCreateActualAvailabilityErrorComponent
        | ApiV1WorkspacesReconcileCreateAlternativeNameErrorComponent
        | ApiV1WorkspacesReconcileCreateAnnotationsErrorComponent
        | ApiV1WorkspacesReconcileCreateArchivedAtErrorComponent
        | ApiV1WorkspacesReconcileCreateArchivedErrorComponent
        | ApiV1WorkspacesReconcileCreateArchivedReasonErrorComponent
        | ApiV1WorkspacesReconcileCreateBackupEnabledErrorComponent
        | ApiV1WorkspacesReconcileCreateCriticalityErrorComponent
        | ApiV1WorkspacesReconcileCreateDebugModeErrorComponent
        | ApiV1WorkspacesReconcileCreateDescriptionErrorComponent
        | ApiV1WorkspacesReconcileCreateDiscoveryEnabledErrorComponent
        | ApiV1WorkspacesReconcileCreateDisplayNameErrorComponent
        | ApiV1WorkspacesReconcileCreateEncryptedErrorComponent
        | ApiV1WorkspacesReconcileCreateEndpointMonitoringModeErrorComponent
        | ApiV1WorkspacesReconcileCreateEndpointMonitorsErrorComponent
        | ApiV1WorkspacesReconcileCreateGitlabProjectIdErrorComponent
        | ApiV1WorkspacesReconcileCreateGitlabProjectUrlErrorComponent
        | ApiV1WorkspacesReconcileCreateGlobalEndpointMonitorErrorComponent
        | ApiV1WorkspacesReconcileCreateHasIncompatibleKubeconfigErrorComponent
        | ApiV1WorkspacesReconcileCreateK8SAddonsEnabledErrorComponent
        | ApiV1WorkspacesReconcileCreateKindErrorComponent
        | ApiV1WorkspacesReconcileCreateLabelsErrorComponent
        | ApiV1WorkspacesReconcileCreateLogsEnabledErrorComponent
        | ApiV1WorkspacesReconcileCreateMetricsEnabledErrorComponent
        | ApiV1WorkspacesReconcileCreateMonitoringWorkspaceAllowlistIdsErrorComponent
        | ApiV1WorkspacesReconcileCreateNameErrorComponent
        | ApiV1WorkspacesReconcileCreateNonFieldErrorsErrorComponent
        | ApiV1WorkspacesReconcileCreateNotificationsEnabledErrorComponent
        | ApiV1WorkspacesReconcileCreateOnPremiseErrorComponent
        | ApiV1WorkspacesReconcileCreateOrganizationIdErrorComponent
        | ApiV1WorkspacesReconcileCreateOwnerIdErrorComponent
        | ApiV1WorkspacesReconcileCreatePlatformServiceErrorComponent
        | ApiV1WorkspacesReconcileCreatePopIdErrorComponent
        | ApiV1WorkspacesReconcileCreateProviderErrorComponent
        | ApiV1WorkspacesReconcileCreateProviderIdErrorComponent
        | ApiV1WorkspacesReconcileCreateProviderReferenceErrorComponent
        | ApiV1WorkspacesReconcileCreatePurposeErrorComponent
        | ApiV1WorkspacesReconcileCreateReadmeMdErrorComponent
        | ApiV1WorkspacesReconcileCreateReconciliationEnabledErrorComponent
        | ApiV1WorkspacesReconcileCreateScopeErrorComponent
        | ApiV1WorkspacesReconcileCreateSecretsPolyRawErrorComponent
        | ApiV1WorkspacesReconcileCreateSlaAvailabilityErrorComponent
        | ApiV1WorkspacesReconcileCreateSlaTargetErrorComponent
        | ApiV1WorkspacesReconcileCreateSloAvailabilityErrorComponent
        | ApiV1WorkspacesReconcileCreateSloTargetErrorComponent
        | ApiV1WorkspacesReconcileCreateTargetAvailabilityErrorComponent
        | ApiV1WorkspacesReconcileCreateTemplateErrorComponent
        | ApiV1WorkspacesReconcileCreateUrlsErrorComponent
        | ApiV1WorkspacesReconcileCreateWorkspaceInventoryRawErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_workspaces_reconcile_create_actual_availability_error_component import (
            ApiV1WorkspacesReconcileCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_annotations_error_component import (
            ApiV1WorkspacesReconcileCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_archived_at_error_component import (
            ApiV1WorkspacesReconcileCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_archived_error_component import (
            ApiV1WorkspacesReconcileCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_archived_reason_error_component import (
            ApiV1WorkspacesReconcileCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_backup_enabled_error_component import (
            ApiV1WorkspacesReconcileCreateBackupEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_criticality_error_component import (
            ApiV1WorkspacesReconcileCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_debug_mode_error_component import (
            ApiV1WorkspacesReconcileCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_description_error_component import (
            ApiV1WorkspacesReconcileCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_discovery_enabled_error_component import (
            ApiV1WorkspacesReconcileCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_display_name_error_component import (
            ApiV1WorkspacesReconcileCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_encrypted_error_component import (
            ApiV1WorkspacesReconcileCreateEncryptedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_endpoint_monitoring_mode_error_component import (
            ApiV1WorkspacesReconcileCreateEndpointMonitoringModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_endpoint_monitors_error_component import (
            ApiV1WorkspacesReconcileCreateEndpointMonitorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_gitlab_project_id_error_component import (
            ApiV1WorkspacesReconcileCreateGitlabProjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_gitlab_project_url_error_component import (
            ApiV1WorkspacesReconcileCreateGitlabProjectUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_global_endpoint_monitor_error_component import (
            ApiV1WorkspacesReconcileCreateGlobalEndpointMonitorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_has_incompatible_kubeconfig_error_component import (
            ApiV1WorkspacesReconcileCreateHasIncompatibleKubeconfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_k8s_addons_enabled_error_component import (
            ApiV1WorkspacesReconcileCreateK8SAddonsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_kind_error_component import (
            ApiV1WorkspacesReconcileCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_labels_error_component import (
            ApiV1WorkspacesReconcileCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_logs_enabled_error_component import (
            ApiV1WorkspacesReconcileCreateLogsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_metrics_enabled_error_component import (
            ApiV1WorkspacesReconcileCreateMetricsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_monitoring_workspace_allowlist_ids_error_component import (
            ApiV1WorkspacesReconcileCreateMonitoringWorkspaceAllowlistIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_name_error_component import (
            ApiV1WorkspacesReconcileCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_non_field_errors_error_component import (
            ApiV1WorkspacesReconcileCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_notifications_enabled_error_component import (
            ApiV1WorkspacesReconcileCreateNotificationsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_on_premise_error_component import (
            ApiV1WorkspacesReconcileCreateOnPremiseErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_organization_id_error_component import (
            ApiV1WorkspacesReconcileCreateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_owner_id_error_component import (
            ApiV1WorkspacesReconcileCreateOwnerIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_platform_service_error_component import (
            ApiV1WorkspacesReconcileCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_pop_id_error_component import (
            ApiV1WorkspacesReconcileCreatePopIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_provider_error_component import (
            ApiV1WorkspacesReconcileCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_provider_id_error_component import (
            ApiV1WorkspacesReconcileCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_provider_reference_error_component import (
            ApiV1WorkspacesReconcileCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_purpose_error_component import (
            ApiV1WorkspacesReconcileCreatePurposeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_readme_md_error_component import (
            ApiV1WorkspacesReconcileCreateReadmeMdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_reconciliation_enabled_error_component import (
            ApiV1WorkspacesReconcileCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_scope_error_component import (
            ApiV1WorkspacesReconcileCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_secrets_poly_raw_error_component import (
            ApiV1WorkspacesReconcileCreateSecretsPolyRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_sla_availability_error_component import (
            ApiV1WorkspacesReconcileCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_sla_target_error_component import (
            ApiV1WorkspacesReconcileCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_slo_availability_error_component import (
            ApiV1WorkspacesReconcileCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_slo_target_error_component import (
            ApiV1WorkspacesReconcileCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_target_availability_error_component import (
            ApiV1WorkspacesReconcileCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_template_error_component import (
            ApiV1WorkspacesReconcileCreateTemplateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_urls_error_component import (
            ApiV1WorkspacesReconcileCreateUrlsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_workspace_inventory_raw_error_component import (
            ApiV1WorkspacesReconcileCreateWorkspaceInventoryRawErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateGitlabProjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateGitlabProjectUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateOnPremiseErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateEndpointMonitoringModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateGlobalEndpointMonitorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesReconcileCreateMonitoringWorkspaceAllowlistIdsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateNotificationsEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateBackupEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateMetricsEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateLogsEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateK8SAddonsEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateHasIncompatibleKubeconfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateEndpointMonitorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateSecretsPolyRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateWorkspaceInventoryRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateEncryptedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreatePopIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateTemplateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreatePurposeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateUrlsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateOwnerIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReconcileCreateReadmeMdErrorComponent):
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
        from ..models.api_v1_workspaces_reconcile_create_actual_availability_error_component import (
            ApiV1WorkspacesReconcileCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_alternative_name_error_component import (
            ApiV1WorkspacesReconcileCreateAlternativeNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_annotations_error_component import (
            ApiV1WorkspacesReconcileCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_archived_at_error_component import (
            ApiV1WorkspacesReconcileCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_archived_error_component import (
            ApiV1WorkspacesReconcileCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_archived_reason_error_component import (
            ApiV1WorkspacesReconcileCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_backup_enabled_error_component import (
            ApiV1WorkspacesReconcileCreateBackupEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_criticality_error_component import (
            ApiV1WorkspacesReconcileCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_debug_mode_error_component import (
            ApiV1WorkspacesReconcileCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_description_error_component import (
            ApiV1WorkspacesReconcileCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_discovery_enabled_error_component import (
            ApiV1WorkspacesReconcileCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_display_name_error_component import (
            ApiV1WorkspacesReconcileCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_encrypted_error_component import (
            ApiV1WorkspacesReconcileCreateEncryptedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_endpoint_monitoring_mode_error_component import (
            ApiV1WorkspacesReconcileCreateEndpointMonitoringModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_endpoint_monitors_error_component import (
            ApiV1WorkspacesReconcileCreateEndpointMonitorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_gitlab_project_id_error_component import (
            ApiV1WorkspacesReconcileCreateGitlabProjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_gitlab_project_url_error_component import (
            ApiV1WorkspacesReconcileCreateGitlabProjectUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_global_endpoint_monitor_error_component import (
            ApiV1WorkspacesReconcileCreateGlobalEndpointMonitorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_has_incompatible_kubeconfig_error_component import (
            ApiV1WorkspacesReconcileCreateHasIncompatibleKubeconfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_k8s_addons_enabled_error_component import (
            ApiV1WorkspacesReconcileCreateK8SAddonsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_kind_error_component import (
            ApiV1WorkspacesReconcileCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_labels_error_component import (
            ApiV1WorkspacesReconcileCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_logs_enabled_error_component import (
            ApiV1WorkspacesReconcileCreateLogsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_metrics_enabled_error_component import (
            ApiV1WorkspacesReconcileCreateMetricsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_monitoring_workspace_allowlist_ids_error_component import (
            ApiV1WorkspacesReconcileCreateMonitoringWorkspaceAllowlistIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_name_error_component import (
            ApiV1WorkspacesReconcileCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_non_field_errors_error_component import (
            ApiV1WorkspacesReconcileCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_notifications_enabled_error_component import (
            ApiV1WorkspacesReconcileCreateNotificationsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_on_premise_error_component import (
            ApiV1WorkspacesReconcileCreateOnPremiseErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_organization_id_error_component import (
            ApiV1WorkspacesReconcileCreateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_owner_id_error_component import (
            ApiV1WorkspacesReconcileCreateOwnerIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_platform_service_error_component import (
            ApiV1WorkspacesReconcileCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_pop_id_error_component import (
            ApiV1WorkspacesReconcileCreatePopIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_provider_error_component import (
            ApiV1WorkspacesReconcileCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_provider_id_error_component import (
            ApiV1WorkspacesReconcileCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_provider_reference_error_component import (
            ApiV1WorkspacesReconcileCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_purpose_error_component import (
            ApiV1WorkspacesReconcileCreatePurposeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_readme_md_error_component import (
            ApiV1WorkspacesReconcileCreateReadmeMdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_reconciliation_enabled_error_component import (
            ApiV1WorkspacesReconcileCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_scope_error_component import (
            ApiV1WorkspacesReconcileCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_secrets_poly_raw_error_component import (
            ApiV1WorkspacesReconcileCreateSecretsPolyRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_sla_availability_error_component import (
            ApiV1WorkspacesReconcileCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_sla_target_error_component import (
            ApiV1WorkspacesReconcileCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_slo_availability_error_component import (
            ApiV1WorkspacesReconcileCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_slo_target_error_component import (
            ApiV1WorkspacesReconcileCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_target_availability_error_component import (
            ApiV1WorkspacesReconcileCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_template_error_component import (
            ApiV1WorkspacesReconcileCreateTemplateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_urls_error_component import (
            ApiV1WorkspacesReconcileCreateUrlsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reconcile_create_workspace_inventory_raw_error_component import (
            ApiV1WorkspacesReconcileCreateWorkspaceInventoryRawErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1WorkspacesReconcileCreateActualAvailabilityErrorComponent
                | ApiV1WorkspacesReconcileCreateAlternativeNameErrorComponent
                | ApiV1WorkspacesReconcileCreateAnnotationsErrorComponent
                | ApiV1WorkspacesReconcileCreateArchivedAtErrorComponent
                | ApiV1WorkspacesReconcileCreateArchivedErrorComponent
                | ApiV1WorkspacesReconcileCreateArchivedReasonErrorComponent
                | ApiV1WorkspacesReconcileCreateBackupEnabledErrorComponent
                | ApiV1WorkspacesReconcileCreateCriticalityErrorComponent
                | ApiV1WorkspacesReconcileCreateDebugModeErrorComponent
                | ApiV1WorkspacesReconcileCreateDescriptionErrorComponent
                | ApiV1WorkspacesReconcileCreateDiscoveryEnabledErrorComponent
                | ApiV1WorkspacesReconcileCreateDisplayNameErrorComponent
                | ApiV1WorkspacesReconcileCreateEncryptedErrorComponent
                | ApiV1WorkspacesReconcileCreateEndpointMonitoringModeErrorComponent
                | ApiV1WorkspacesReconcileCreateEndpointMonitorsErrorComponent
                | ApiV1WorkspacesReconcileCreateGitlabProjectIdErrorComponent
                | ApiV1WorkspacesReconcileCreateGitlabProjectUrlErrorComponent
                | ApiV1WorkspacesReconcileCreateGlobalEndpointMonitorErrorComponent
                | ApiV1WorkspacesReconcileCreateHasIncompatibleKubeconfigErrorComponent
                | ApiV1WorkspacesReconcileCreateK8SAddonsEnabledErrorComponent
                | ApiV1WorkspacesReconcileCreateKindErrorComponent
                | ApiV1WorkspacesReconcileCreateLabelsErrorComponent
                | ApiV1WorkspacesReconcileCreateLogsEnabledErrorComponent
                | ApiV1WorkspacesReconcileCreateMetricsEnabledErrorComponent
                | ApiV1WorkspacesReconcileCreateMonitoringWorkspaceAllowlistIdsErrorComponent
                | ApiV1WorkspacesReconcileCreateNameErrorComponent
                | ApiV1WorkspacesReconcileCreateNonFieldErrorsErrorComponent
                | ApiV1WorkspacesReconcileCreateNotificationsEnabledErrorComponent
                | ApiV1WorkspacesReconcileCreateOnPremiseErrorComponent
                | ApiV1WorkspacesReconcileCreateOrganizationIdErrorComponent
                | ApiV1WorkspacesReconcileCreateOwnerIdErrorComponent
                | ApiV1WorkspacesReconcileCreatePlatformServiceErrorComponent
                | ApiV1WorkspacesReconcileCreatePopIdErrorComponent
                | ApiV1WorkspacesReconcileCreateProviderErrorComponent
                | ApiV1WorkspacesReconcileCreateProviderIdErrorComponent
                | ApiV1WorkspacesReconcileCreateProviderReferenceErrorComponent
                | ApiV1WorkspacesReconcileCreatePurposeErrorComponent
                | ApiV1WorkspacesReconcileCreateReadmeMdErrorComponent
                | ApiV1WorkspacesReconcileCreateReconciliationEnabledErrorComponent
                | ApiV1WorkspacesReconcileCreateScopeErrorComponent
                | ApiV1WorkspacesReconcileCreateSecretsPolyRawErrorComponent
                | ApiV1WorkspacesReconcileCreateSlaAvailabilityErrorComponent
                | ApiV1WorkspacesReconcileCreateSlaTargetErrorComponent
                | ApiV1WorkspacesReconcileCreateSloAvailabilityErrorComponent
                | ApiV1WorkspacesReconcileCreateSloTargetErrorComponent
                | ApiV1WorkspacesReconcileCreateTargetAvailabilityErrorComponent
                | ApiV1WorkspacesReconcileCreateTemplateErrorComponent
                | ApiV1WorkspacesReconcileCreateUrlsErrorComponent
                | ApiV1WorkspacesReconcileCreateWorkspaceInventoryRawErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_0 = (
                        ApiV1WorkspacesReconcileCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_1 = (
                        ApiV1WorkspacesReconcileCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_2 = (
                        ApiV1WorkspacesReconcileCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_3 = (
                        ApiV1WorkspacesReconcileCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_4 = (
                        ApiV1WorkspacesReconcileCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_5 = (
                        ApiV1WorkspacesReconcileCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_6 = (
                        ApiV1WorkspacesReconcileCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_7 = (
                        ApiV1WorkspacesReconcileCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_8 = (
                        ApiV1WorkspacesReconcileCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_9 = (
                        ApiV1WorkspacesReconcileCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_10 = (
                        ApiV1WorkspacesReconcileCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_11 = (
                        ApiV1WorkspacesReconcileCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_12 = (
                        ApiV1WorkspacesReconcileCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_13 = (
                        ApiV1WorkspacesReconcileCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_14 = (
                        ApiV1WorkspacesReconcileCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_15 = (
                        ApiV1WorkspacesReconcileCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_16 = (
                        ApiV1WorkspacesReconcileCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_17 = (
                        ApiV1WorkspacesReconcileCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_18 = (
                        ApiV1WorkspacesReconcileCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_19 = (
                        ApiV1WorkspacesReconcileCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_20 = (
                        ApiV1WorkspacesReconcileCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_21 = (
                        ApiV1WorkspacesReconcileCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_22 = (
                        ApiV1WorkspacesReconcileCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_23 = (
                        ApiV1WorkspacesReconcileCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_24 = (
                        ApiV1WorkspacesReconcileCreateGitlabProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_25 = (
                        ApiV1WorkspacesReconcileCreateGitlabProjectUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_26 = (
                        ApiV1WorkspacesReconcileCreateOnPremiseErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_27 = (
                        ApiV1WorkspacesReconcileCreateEndpointMonitoringModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_28 = (
                        ApiV1WorkspacesReconcileCreateGlobalEndpointMonitorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_29 = (
                        ApiV1WorkspacesReconcileCreateMonitoringWorkspaceAllowlistIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_30 = (
                        ApiV1WorkspacesReconcileCreateNotificationsEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_31 = (
                        ApiV1WorkspacesReconcileCreateBackupEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_32 = (
                        ApiV1WorkspacesReconcileCreateMetricsEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_33 = (
                        ApiV1WorkspacesReconcileCreateLogsEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_34 = (
                        ApiV1WorkspacesReconcileCreateK8SAddonsEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_35 = (
                        ApiV1WorkspacesReconcileCreateHasIncompatibleKubeconfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_36 = (
                        ApiV1WorkspacesReconcileCreateEndpointMonitorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_37 = (
                        ApiV1WorkspacesReconcileCreateSecretsPolyRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_38 = (
                        ApiV1WorkspacesReconcileCreateWorkspaceInventoryRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_39 = (
                        ApiV1WorkspacesReconcileCreateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_40 = (
                        ApiV1WorkspacesReconcileCreateEncryptedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_41 = (
                        ApiV1WorkspacesReconcileCreatePopIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_42 = (
                        ApiV1WorkspacesReconcileCreateTemplateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_43 = (
                        ApiV1WorkspacesReconcileCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_44 = (
                        ApiV1WorkspacesReconcileCreatePurposeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_45 = (
                        ApiV1WorkspacesReconcileCreateUrlsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_46 = (
                        ApiV1WorkspacesReconcileCreateOwnerIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reconcile_create_error_type_47 = (
                        ApiV1WorkspacesReconcileCreateReadmeMdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reconcile_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_workspaces_reconcile_create_error_type_48 = (
                    ApiV1WorkspacesReconcileCreateAlternativeNameErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_workspaces_reconcile_create_error_type_48

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_workspaces_reconcile_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_workspaces_reconcile_create_validation_error.additional_properties = d
        return api_v1_workspaces_reconcile_create_validation_error

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
