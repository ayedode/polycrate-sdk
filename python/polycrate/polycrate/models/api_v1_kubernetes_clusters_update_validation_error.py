from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_clusters_update_active_error_component import (
        ApiV1KubernetesClustersUpdateActiveErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_actual_availability_error_component import (
        ApiV1KubernetesClustersUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_addons_error_component import (
        ApiV1KubernetesClustersUpdateAddonsErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_alias_error_component import (
        ApiV1KubernetesClustersUpdateAliasErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_annotations_error_component import (
        ApiV1KubernetesClustersUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_api_server_cert_expiry_date_error_component import (
        ApiV1KubernetesClustersUpdateApiServerCertExpiryDateErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_archived_at_error_component import (
        ApiV1KubernetesClustersUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_archived_error_component import (
        ApiV1KubernetesClustersUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_archived_reason_error_component import (
        ApiV1KubernetesClustersUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_backup_schedules_error_component import (
        ApiV1KubernetesClustersUpdateBackupSchedulesErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_baserow_id_error_component import (
        ApiV1KubernetesClustersUpdateBaserowIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_credential_error_component import (
        ApiV1KubernetesClustersUpdateCredentialErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_criticality_error_component import (
        ApiV1KubernetesClustersUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_debug_mode_error_component import (
        ApiV1KubernetesClustersUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_description_error_component import (
        ApiV1KubernetesClustersUpdateDescriptionErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_discovery_enabled_error_component import (
        ApiV1KubernetesClustersUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_discovery_ignored_namespaces_error_component import (
        ApiV1KubernetesClustersUpdateDiscoveryIgnoredNamespacesErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_display_name_error_component import (
        ApiV1KubernetesClustersUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_gitlab_project_id_error_component import (
        ApiV1KubernetesClustersUpdateGitlabProjectIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_installed_error_component import (
        ApiV1KubernetesClustersUpdateInstalledErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_is_host_cluster_error_component import (
        ApiV1KubernetesClustersUpdateIsHostClusterErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_is_infrastructure_cluster_error_component import (
        ApiV1KubernetesClustersUpdateIsInfrastructureClusterErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_kind_error_component import (
        ApiV1KubernetesClustersUpdateKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_kubeconfig_ca_cert_expiry_date_error_component import (
        ApiV1KubernetesClustersUpdateKubeconfigCaCertExpiryDateErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_kubeconfig_client_cert_expiry_date_error_component import (
        ApiV1KubernetesClustersUpdateKubeconfigClientCertExpiryDateErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_kubernetes_version_error_component import (
        ApiV1KubernetesClustersUpdateKubernetesVersionErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_labels_error_component import (
        ApiV1KubernetesClustersUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_last_backup_import_error_component import (
        ApiV1KubernetesClustersUpdateLastBackupImportErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_managed_by_content_type_error_component import (
        ApiV1KubernetesClustersUpdateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_managed_by_object_id_error_component import (
        ApiV1KubernetesClustersUpdateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_name_error_component import (
        ApiV1KubernetesClustersUpdateNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_non_field_errors_error_component import (
        ApiV1KubernetesClustersUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_operator_ignore_namespaces_error_component import (
        ApiV1KubernetesClustersUpdateOperatorIgnoreNamespacesErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_operator_loglevel_error_component import (
        ApiV1KubernetesClustersUpdateOperatorLoglevelErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_platform_dns_record_created_error_component import (
        ApiV1KubernetesClustersUpdatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_platform_service_error_component import (
        ApiV1KubernetesClustersUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_provider_error_component import (
        ApiV1KubernetesClustersUpdateProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_provider_id_error_component import (
        ApiV1KubernetesClustersUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_provider_reference_error_component import (
        ApiV1KubernetesClustersUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_reconciliation_enabled_error_component import (
        ApiV1KubernetesClustersUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_scope_error_component import (
        ApiV1KubernetesClustersUpdateScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_sla_availability_error_component import (
        ApiV1KubernetesClustersUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_sla_target_error_component import (
        ApiV1KubernetesClustersUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_slo_availability_error_component import (
        ApiV1KubernetesClustersUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_slo_target_error_component import (
        ApiV1KubernetesClustersUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_slug_error_component import (
        ApiV1KubernetesClustersUpdateSlugErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_update_target_availability_error_component import (
        ApiV1KubernetesClustersUpdateTargetAvailabilityErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesClustersUpdateValidationError")


@_attrs_define
class ApiV1KubernetesClustersUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesClustersUpdateActiveErrorComponent |
            ApiV1KubernetesClustersUpdateActualAvailabilityErrorComponent |
            ApiV1KubernetesClustersUpdateAddonsErrorComponent | ApiV1KubernetesClustersUpdateAliasErrorComponent |
            ApiV1KubernetesClustersUpdateAnnotationsErrorComponent |
            ApiV1KubernetesClustersUpdateApiServerCertExpiryDateErrorComponent |
            ApiV1KubernetesClustersUpdateArchivedAtErrorComponent | ApiV1KubernetesClustersUpdateArchivedErrorComponent |
            ApiV1KubernetesClustersUpdateArchivedReasonErrorComponent |
            ApiV1KubernetesClustersUpdateBackupSchedulesErrorComponent |
            ApiV1KubernetesClustersUpdateBaserowIdErrorComponent | ApiV1KubernetesClustersUpdateCredentialErrorComponent |
            ApiV1KubernetesClustersUpdateCriticalityErrorComponent | ApiV1KubernetesClustersUpdateDebugModeErrorComponent |
            ApiV1KubernetesClustersUpdateDescriptionErrorComponent |
            ApiV1KubernetesClustersUpdateDiscoveryEnabledErrorComponent |
            ApiV1KubernetesClustersUpdateDiscoveryIgnoredNamespacesErrorComponent |
            ApiV1KubernetesClustersUpdateDisplayNameErrorComponent |
            ApiV1KubernetesClustersUpdateGitlabProjectIdErrorComponent |
            ApiV1KubernetesClustersUpdateInstalledErrorComponent | ApiV1KubernetesClustersUpdateIsHostClusterErrorComponent
            | ApiV1KubernetesClustersUpdateIsInfrastructureClusterErrorComponent |
            ApiV1KubernetesClustersUpdateKindErrorComponent |
            ApiV1KubernetesClustersUpdateKubeconfigCaCertExpiryDateErrorComponent |
            ApiV1KubernetesClustersUpdateKubeconfigClientCertExpiryDateErrorComponent |
            ApiV1KubernetesClustersUpdateKubernetesVersionErrorComponent | ApiV1KubernetesClustersUpdateLabelsErrorComponent
            | ApiV1KubernetesClustersUpdateLastBackupImportErrorComponent |
            ApiV1KubernetesClustersUpdateManagedByContentTypeErrorComponent |
            ApiV1KubernetesClustersUpdateManagedByObjectIdErrorComponent | ApiV1KubernetesClustersUpdateNameErrorComponent |
            ApiV1KubernetesClustersUpdateNonFieldErrorsErrorComponent |
            ApiV1KubernetesClustersUpdateOperatorIgnoreNamespacesErrorComponent |
            ApiV1KubernetesClustersUpdateOperatorLoglevelErrorComponent |
            ApiV1KubernetesClustersUpdatePlatformDnsRecordCreatedErrorComponent |
            ApiV1KubernetesClustersUpdatePlatformServiceErrorComponent | ApiV1KubernetesClustersUpdateProviderErrorComponent
            | ApiV1KubernetesClustersUpdateProviderIdErrorComponent |
            ApiV1KubernetesClustersUpdateProviderReferenceErrorComponent |
            ApiV1KubernetesClustersUpdateReconciliationEnabledErrorComponent |
            ApiV1KubernetesClustersUpdateScopeErrorComponent | ApiV1KubernetesClustersUpdateSlaAvailabilityErrorComponent |
            ApiV1KubernetesClustersUpdateSlaTargetErrorComponent |
            ApiV1KubernetesClustersUpdateSloAvailabilityErrorComponent |
            ApiV1KubernetesClustersUpdateSloTargetErrorComponent | ApiV1KubernetesClustersUpdateSlugErrorComponent |
            ApiV1KubernetesClustersUpdateTargetAvailabilityErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesClustersUpdateActiveErrorComponent
        | ApiV1KubernetesClustersUpdateActualAvailabilityErrorComponent
        | ApiV1KubernetesClustersUpdateAddonsErrorComponent
        | ApiV1KubernetesClustersUpdateAliasErrorComponent
        | ApiV1KubernetesClustersUpdateAnnotationsErrorComponent
        | ApiV1KubernetesClustersUpdateApiServerCertExpiryDateErrorComponent
        | ApiV1KubernetesClustersUpdateArchivedAtErrorComponent
        | ApiV1KubernetesClustersUpdateArchivedErrorComponent
        | ApiV1KubernetesClustersUpdateArchivedReasonErrorComponent
        | ApiV1KubernetesClustersUpdateBackupSchedulesErrorComponent
        | ApiV1KubernetesClustersUpdateBaserowIdErrorComponent
        | ApiV1KubernetesClustersUpdateCredentialErrorComponent
        | ApiV1KubernetesClustersUpdateCriticalityErrorComponent
        | ApiV1KubernetesClustersUpdateDebugModeErrorComponent
        | ApiV1KubernetesClustersUpdateDescriptionErrorComponent
        | ApiV1KubernetesClustersUpdateDiscoveryEnabledErrorComponent
        | ApiV1KubernetesClustersUpdateDiscoveryIgnoredNamespacesErrorComponent
        | ApiV1KubernetesClustersUpdateDisplayNameErrorComponent
        | ApiV1KubernetesClustersUpdateGitlabProjectIdErrorComponent
        | ApiV1KubernetesClustersUpdateInstalledErrorComponent
        | ApiV1KubernetesClustersUpdateIsHostClusterErrorComponent
        | ApiV1KubernetesClustersUpdateIsInfrastructureClusterErrorComponent
        | ApiV1KubernetesClustersUpdateKindErrorComponent
        | ApiV1KubernetesClustersUpdateKubeconfigCaCertExpiryDateErrorComponent
        | ApiV1KubernetesClustersUpdateKubeconfigClientCertExpiryDateErrorComponent
        | ApiV1KubernetesClustersUpdateKubernetesVersionErrorComponent
        | ApiV1KubernetesClustersUpdateLabelsErrorComponent
        | ApiV1KubernetesClustersUpdateLastBackupImportErrorComponent
        | ApiV1KubernetesClustersUpdateManagedByContentTypeErrorComponent
        | ApiV1KubernetesClustersUpdateManagedByObjectIdErrorComponent
        | ApiV1KubernetesClustersUpdateNameErrorComponent
        | ApiV1KubernetesClustersUpdateNonFieldErrorsErrorComponent
        | ApiV1KubernetesClustersUpdateOperatorIgnoreNamespacesErrorComponent
        | ApiV1KubernetesClustersUpdateOperatorLoglevelErrorComponent
        | ApiV1KubernetesClustersUpdatePlatformDnsRecordCreatedErrorComponent
        | ApiV1KubernetesClustersUpdatePlatformServiceErrorComponent
        | ApiV1KubernetesClustersUpdateProviderErrorComponent
        | ApiV1KubernetesClustersUpdateProviderIdErrorComponent
        | ApiV1KubernetesClustersUpdateProviderReferenceErrorComponent
        | ApiV1KubernetesClustersUpdateReconciliationEnabledErrorComponent
        | ApiV1KubernetesClustersUpdateScopeErrorComponent
        | ApiV1KubernetesClustersUpdateSlaAvailabilityErrorComponent
        | ApiV1KubernetesClustersUpdateSlaTargetErrorComponent
        | ApiV1KubernetesClustersUpdateSloAvailabilityErrorComponent
        | ApiV1KubernetesClustersUpdateSloTargetErrorComponent
        | ApiV1KubernetesClustersUpdateSlugErrorComponent
        | ApiV1KubernetesClustersUpdateTargetAvailabilityErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_clusters_update_active_error_component import (
            ApiV1KubernetesClustersUpdateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_actual_availability_error_component import (
            ApiV1KubernetesClustersUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_addons_error_component import (
            ApiV1KubernetesClustersUpdateAddonsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_alias_error_component import (
            ApiV1KubernetesClustersUpdateAliasErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_annotations_error_component import (
            ApiV1KubernetesClustersUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_api_server_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersUpdateApiServerCertExpiryDateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_archived_at_error_component import (
            ApiV1KubernetesClustersUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_archived_error_component import (
            ApiV1KubernetesClustersUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_archived_reason_error_component import (
            ApiV1KubernetesClustersUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_backup_schedules_error_component import (
            ApiV1KubernetesClustersUpdateBackupSchedulesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_baserow_id_error_component import (
            ApiV1KubernetesClustersUpdateBaserowIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_credential_error_component import (
            ApiV1KubernetesClustersUpdateCredentialErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_criticality_error_component import (
            ApiV1KubernetesClustersUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_debug_mode_error_component import (
            ApiV1KubernetesClustersUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_description_error_component import (
            ApiV1KubernetesClustersUpdateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_discovery_enabled_error_component import (
            ApiV1KubernetesClustersUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_discovery_ignored_namespaces_error_component import (
            ApiV1KubernetesClustersUpdateDiscoveryIgnoredNamespacesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_display_name_error_component import (
            ApiV1KubernetesClustersUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_gitlab_project_id_error_component import (
            ApiV1KubernetesClustersUpdateGitlabProjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_installed_error_component import (
            ApiV1KubernetesClustersUpdateInstalledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_is_host_cluster_error_component import (
            ApiV1KubernetesClustersUpdateIsHostClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_is_infrastructure_cluster_error_component import (
            ApiV1KubernetesClustersUpdateIsInfrastructureClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_kind_error_component import (
            ApiV1KubernetesClustersUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_kubeconfig_ca_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersUpdateKubeconfigCaCertExpiryDateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_kubeconfig_client_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersUpdateKubeconfigClientCertExpiryDateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_kubernetes_version_error_component import (
            ApiV1KubernetesClustersUpdateKubernetesVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_labels_error_component import (
            ApiV1KubernetesClustersUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_last_backup_import_error_component import (
            ApiV1KubernetesClustersUpdateLastBackupImportErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_managed_by_content_type_error_component import (
            ApiV1KubernetesClustersUpdateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_name_error_component import (
            ApiV1KubernetesClustersUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_non_field_errors_error_component import (
            ApiV1KubernetesClustersUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_operator_ignore_namespaces_error_component import (
            ApiV1KubernetesClustersUpdateOperatorIgnoreNamespacesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_operator_loglevel_error_component import (
            ApiV1KubernetesClustersUpdateOperatorLoglevelErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_platform_dns_record_created_error_component import (
            ApiV1KubernetesClustersUpdatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_platform_service_error_component import (
            ApiV1KubernetesClustersUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_provider_error_component import (
            ApiV1KubernetesClustersUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_provider_id_error_component import (
            ApiV1KubernetesClustersUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_provider_reference_error_component import (
            ApiV1KubernetesClustersUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_reconciliation_enabled_error_component import (
            ApiV1KubernetesClustersUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_scope_error_component import (
            ApiV1KubernetesClustersUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_sla_availability_error_component import (
            ApiV1KubernetesClustersUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_sla_target_error_component import (
            ApiV1KubernetesClustersUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_slo_availability_error_component import (
            ApiV1KubernetesClustersUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_slo_target_error_component import (
            ApiV1KubernetesClustersUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_slug_error_component import (
            ApiV1KubernetesClustersUpdateSlugErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_target_availability_error_component import (
            ApiV1KubernetesClustersUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesClustersUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdateKubernetesVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdateInstalledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdateIsHostClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdateIsInfrastructureClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdateKubeconfigCaCertExpiryDateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersUpdateKubeconfigClientCertExpiryDateErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdateApiServerCertExpiryDateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdateCredentialErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdateDiscoveryIgnoredNamespacesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdateOperatorLoglevelErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdateOperatorIgnoreNamespacesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdateAliasErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdateAddonsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdateBackupSchedulesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdateBaserowIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdateGitlabProjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdateLastBackupImportErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdateSlugErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersUpdateManagedByContentTypeErrorComponent):
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
        from ..models.api_v1_kubernetes_clusters_update_active_error_component import (
            ApiV1KubernetesClustersUpdateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_actual_availability_error_component import (
            ApiV1KubernetesClustersUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_addons_error_component import (
            ApiV1KubernetesClustersUpdateAddonsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_alias_error_component import (
            ApiV1KubernetesClustersUpdateAliasErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_annotations_error_component import (
            ApiV1KubernetesClustersUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_api_server_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersUpdateApiServerCertExpiryDateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_archived_at_error_component import (
            ApiV1KubernetesClustersUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_archived_error_component import (
            ApiV1KubernetesClustersUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_archived_reason_error_component import (
            ApiV1KubernetesClustersUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_backup_schedules_error_component import (
            ApiV1KubernetesClustersUpdateBackupSchedulesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_baserow_id_error_component import (
            ApiV1KubernetesClustersUpdateBaserowIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_credential_error_component import (
            ApiV1KubernetesClustersUpdateCredentialErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_criticality_error_component import (
            ApiV1KubernetesClustersUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_debug_mode_error_component import (
            ApiV1KubernetesClustersUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_description_error_component import (
            ApiV1KubernetesClustersUpdateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_discovery_enabled_error_component import (
            ApiV1KubernetesClustersUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_discovery_ignored_namespaces_error_component import (
            ApiV1KubernetesClustersUpdateDiscoveryIgnoredNamespacesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_display_name_error_component import (
            ApiV1KubernetesClustersUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_gitlab_project_id_error_component import (
            ApiV1KubernetesClustersUpdateGitlabProjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_installed_error_component import (
            ApiV1KubernetesClustersUpdateInstalledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_is_host_cluster_error_component import (
            ApiV1KubernetesClustersUpdateIsHostClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_is_infrastructure_cluster_error_component import (
            ApiV1KubernetesClustersUpdateIsInfrastructureClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_kind_error_component import (
            ApiV1KubernetesClustersUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_kubeconfig_ca_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersUpdateKubeconfigCaCertExpiryDateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_kubeconfig_client_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersUpdateKubeconfigClientCertExpiryDateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_kubernetes_version_error_component import (
            ApiV1KubernetesClustersUpdateKubernetesVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_labels_error_component import (
            ApiV1KubernetesClustersUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_last_backup_import_error_component import (
            ApiV1KubernetesClustersUpdateLastBackupImportErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_managed_by_content_type_error_component import (
            ApiV1KubernetesClustersUpdateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_managed_by_object_id_error_component import (
            ApiV1KubernetesClustersUpdateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_name_error_component import (
            ApiV1KubernetesClustersUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_non_field_errors_error_component import (
            ApiV1KubernetesClustersUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_operator_ignore_namespaces_error_component import (
            ApiV1KubernetesClustersUpdateOperatorIgnoreNamespacesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_operator_loglevel_error_component import (
            ApiV1KubernetesClustersUpdateOperatorLoglevelErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_platform_dns_record_created_error_component import (
            ApiV1KubernetesClustersUpdatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_platform_service_error_component import (
            ApiV1KubernetesClustersUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_provider_error_component import (
            ApiV1KubernetesClustersUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_provider_id_error_component import (
            ApiV1KubernetesClustersUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_provider_reference_error_component import (
            ApiV1KubernetesClustersUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_reconciliation_enabled_error_component import (
            ApiV1KubernetesClustersUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_scope_error_component import (
            ApiV1KubernetesClustersUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_sla_availability_error_component import (
            ApiV1KubernetesClustersUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_sla_target_error_component import (
            ApiV1KubernetesClustersUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_slo_availability_error_component import (
            ApiV1KubernetesClustersUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_slo_target_error_component import (
            ApiV1KubernetesClustersUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_slug_error_component import (
            ApiV1KubernetesClustersUpdateSlugErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_update_target_availability_error_component import (
            ApiV1KubernetesClustersUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesClustersUpdateActiveErrorComponent
                | ApiV1KubernetesClustersUpdateActualAvailabilityErrorComponent
                | ApiV1KubernetesClustersUpdateAddonsErrorComponent
                | ApiV1KubernetesClustersUpdateAliasErrorComponent
                | ApiV1KubernetesClustersUpdateAnnotationsErrorComponent
                | ApiV1KubernetesClustersUpdateApiServerCertExpiryDateErrorComponent
                | ApiV1KubernetesClustersUpdateArchivedAtErrorComponent
                | ApiV1KubernetesClustersUpdateArchivedErrorComponent
                | ApiV1KubernetesClustersUpdateArchivedReasonErrorComponent
                | ApiV1KubernetesClustersUpdateBackupSchedulesErrorComponent
                | ApiV1KubernetesClustersUpdateBaserowIdErrorComponent
                | ApiV1KubernetesClustersUpdateCredentialErrorComponent
                | ApiV1KubernetesClustersUpdateCriticalityErrorComponent
                | ApiV1KubernetesClustersUpdateDebugModeErrorComponent
                | ApiV1KubernetesClustersUpdateDescriptionErrorComponent
                | ApiV1KubernetesClustersUpdateDiscoveryEnabledErrorComponent
                | ApiV1KubernetesClustersUpdateDiscoveryIgnoredNamespacesErrorComponent
                | ApiV1KubernetesClustersUpdateDisplayNameErrorComponent
                | ApiV1KubernetesClustersUpdateGitlabProjectIdErrorComponent
                | ApiV1KubernetesClustersUpdateInstalledErrorComponent
                | ApiV1KubernetesClustersUpdateIsHostClusterErrorComponent
                | ApiV1KubernetesClustersUpdateIsInfrastructureClusterErrorComponent
                | ApiV1KubernetesClustersUpdateKindErrorComponent
                | ApiV1KubernetesClustersUpdateKubeconfigCaCertExpiryDateErrorComponent
                | ApiV1KubernetesClustersUpdateKubeconfigClientCertExpiryDateErrorComponent
                | ApiV1KubernetesClustersUpdateKubernetesVersionErrorComponent
                | ApiV1KubernetesClustersUpdateLabelsErrorComponent
                | ApiV1KubernetesClustersUpdateLastBackupImportErrorComponent
                | ApiV1KubernetesClustersUpdateManagedByContentTypeErrorComponent
                | ApiV1KubernetesClustersUpdateManagedByObjectIdErrorComponent
                | ApiV1KubernetesClustersUpdateNameErrorComponent
                | ApiV1KubernetesClustersUpdateNonFieldErrorsErrorComponent
                | ApiV1KubernetesClustersUpdateOperatorIgnoreNamespacesErrorComponent
                | ApiV1KubernetesClustersUpdateOperatorLoglevelErrorComponent
                | ApiV1KubernetesClustersUpdatePlatformDnsRecordCreatedErrorComponent
                | ApiV1KubernetesClustersUpdatePlatformServiceErrorComponent
                | ApiV1KubernetesClustersUpdateProviderErrorComponent
                | ApiV1KubernetesClustersUpdateProviderIdErrorComponent
                | ApiV1KubernetesClustersUpdateProviderReferenceErrorComponent
                | ApiV1KubernetesClustersUpdateReconciliationEnabledErrorComponent
                | ApiV1KubernetesClustersUpdateScopeErrorComponent
                | ApiV1KubernetesClustersUpdateSlaAvailabilityErrorComponent
                | ApiV1KubernetesClustersUpdateSlaTargetErrorComponent
                | ApiV1KubernetesClustersUpdateSloAvailabilityErrorComponent
                | ApiV1KubernetesClustersUpdateSloTargetErrorComponent
                | ApiV1KubernetesClustersUpdateSlugErrorComponent
                | ApiV1KubernetesClustersUpdateTargetAvailabilityErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_0 = (
                        ApiV1KubernetesClustersUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_1 = (
                        ApiV1KubernetesClustersUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_2 = (
                        ApiV1KubernetesClustersUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_3 = (
                        ApiV1KubernetesClustersUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_4 = (
                        ApiV1KubernetesClustersUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_5 = (
                        ApiV1KubernetesClustersUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_6 = (
                        ApiV1KubernetesClustersUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_7 = (
                        ApiV1KubernetesClustersUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_8 = (
                        ApiV1KubernetesClustersUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_9 = (
                        ApiV1KubernetesClustersUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_10 = (
                        ApiV1KubernetesClustersUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_11 = (
                        ApiV1KubernetesClustersUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_12 = (
                        ApiV1KubernetesClustersUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_13 = (
                        ApiV1KubernetesClustersUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_14 = (
                        ApiV1KubernetesClustersUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_15 = (
                        ApiV1KubernetesClustersUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_16 = (
                        ApiV1KubernetesClustersUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_17 = (
                        ApiV1KubernetesClustersUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_18 = (
                        ApiV1KubernetesClustersUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_19 = (
                        ApiV1KubernetesClustersUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_20 = (
                        ApiV1KubernetesClustersUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_21 = (
                        ApiV1KubernetesClustersUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_22 = (
                        ApiV1KubernetesClustersUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_23 = (
                        ApiV1KubernetesClustersUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_24 = (
                        ApiV1KubernetesClustersUpdateKubernetesVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_25 = (
                        ApiV1KubernetesClustersUpdateInstalledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_26 = (
                        ApiV1KubernetesClustersUpdateIsHostClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_27 = (
                        ApiV1KubernetesClustersUpdateIsInfrastructureClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_28 = (
                        ApiV1KubernetesClustersUpdateKubeconfigCaCertExpiryDateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_29 = (
                        ApiV1KubernetesClustersUpdateKubeconfigClientCertExpiryDateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_30 = (
                        ApiV1KubernetesClustersUpdateApiServerCertExpiryDateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_31 = (
                        ApiV1KubernetesClustersUpdateCredentialErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_32 = (
                        ApiV1KubernetesClustersUpdateDiscoveryIgnoredNamespacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_33 = (
                        ApiV1KubernetesClustersUpdateOperatorLoglevelErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_34 = (
                        ApiV1KubernetesClustersUpdateOperatorIgnoreNamespacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_35 = (
                        ApiV1KubernetesClustersUpdateAliasErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_36 = (
                        ApiV1KubernetesClustersUpdateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_37 = (
                        ApiV1KubernetesClustersUpdateAddonsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_38 = (
                        ApiV1KubernetesClustersUpdateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_39 = (
                        ApiV1KubernetesClustersUpdateBackupSchedulesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_40 = (
                        ApiV1KubernetesClustersUpdateBaserowIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_41 = (
                        ApiV1KubernetesClustersUpdateGitlabProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_42 = (
                        ApiV1KubernetesClustersUpdateLastBackupImportErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_43 = (
                        ApiV1KubernetesClustersUpdatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_44 = (
                        ApiV1KubernetesClustersUpdateSlugErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_update_error_type_45 = (
                        ApiV1KubernetesClustersUpdateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_update_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_clusters_update_error_type_46 = (
                    ApiV1KubernetesClustersUpdateManagedByObjectIdErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_clusters_update_error_type_46

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_clusters_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_clusters_update_validation_error.additional_properties = d
        return api_v1_kubernetes_clusters_update_validation_error

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
