from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_clusters_reconcile_create_active_error_component import (
        ApiV1KubernetesClustersReconcileCreateActiveErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_actual_availability_error_component import (
        ApiV1KubernetesClustersReconcileCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_addons_error_component import (
        ApiV1KubernetesClustersReconcileCreateAddonsErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_alias_error_component import (
        ApiV1KubernetesClustersReconcileCreateAliasErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_annotations_error_component import (
        ApiV1KubernetesClustersReconcileCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_api_server_cert_expiry_date_error_component import (
        ApiV1KubernetesClustersReconcileCreateApiServerCertExpiryDateErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_archived_at_error_component import (
        ApiV1KubernetesClustersReconcileCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_archived_error_component import (
        ApiV1KubernetesClustersReconcileCreateArchivedErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_archived_reason_error_component import (
        ApiV1KubernetesClustersReconcileCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_backup_schedules_error_component import (
        ApiV1KubernetesClustersReconcileCreateBackupSchedulesErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_baserow_id_error_component import (
        ApiV1KubernetesClustersReconcileCreateBaserowIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_credential_error_component import (
        ApiV1KubernetesClustersReconcileCreateCredentialErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_criticality_error_component import (
        ApiV1KubernetesClustersReconcileCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_debug_mode_error_component import (
        ApiV1KubernetesClustersReconcileCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_description_error_component import (
        ApiV1KubernetesClustersReconcileCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_discovery_enabled_error_component import (
        ApiV1KubernetesClustersReconcileCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_discovery_ignored_namespaces_error_component import (
        ApiV1KubernetesClustersReconcileCreateDiscoveryIgnoredNamespacesErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_display_name_error_component import (
        ApiV1KubernetesClustersReconcileCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_gitlab_project_id_error_component import (
        ApiV1KubernetesClustersReconcileCreateGitlabProjectIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_installed_error_component import (
        ApiV1KubernetesClustersReconcileCreateInstalledErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_is_host_cluster_error_component import (
        ApiV1KubernetesClustersReconcileCreateIsHostClusterErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_is_infrastructure_cluster_error_component import (
        ApiV1KubernetesClustersReconcileCreateIsInfrastructureClusterErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_kind_error_component import (
        ApiV1KubernetesClustersReconcileCreateKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_kubeconfig_ca_cert_expiry_date_error_component import (
        ApiV1KubernetesClustersReconcileCreateKubeconfigCaCertExpiryDateErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_kubeconfig_client_cert_expiry_date_error_component import (
        ApiV1KubernetesClustersReconcileCreateKubeconfigClientCertExpiryDateErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_kubernetes_version_error_component import (
        ApiV1KubernetesClustersReconcileCreateKubernetesVersionErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_labels_error_component import (
        ApiV1KubernetesClustersReconcileCreateLabelsErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_last_backup_import_error_component import (
        ApiV1KubernetesClustersReconcileCreateLastBackupImportErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_managed_by_content_type_error_component import (
        ApiV1KubernetesClustersReconcileCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_managed_by_object_id_error_component import (
        ApiV1KubernetesClustersReconcileCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_name_error_component import (
        ApiV1KubernetesClustersReconcileCreateNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_non_field_errors_error_component import (
        ApiV1KubernetesClustersReconcileCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_operator_ignore_namespaces_error_component import (
        ApiV1KubernetesClustersReconcileCreateOperatorIgnoreNamespacesErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_operator_loglevel_error_component import (
        ApiV1KubernetesClustersReconcileCreateOperatorLoglevelErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_platform_dns_record_created_error_component import (
        ApiV1KubernetesClustersReconcileCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_platform_service_error_component import (
        ApiV1KubernetesClustersReconcileCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_provider_error_component import (
        ApiV1KubernetesClustersReconcileCreateProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_provider_id_error_component import (
        ApiV1KubernetesClustersReconcileCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_provider_reference_error_component import (
        ApiV1KubernetesClustersReconcileCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_reconciliation_enabled_error_component import (
        ApiV1KubernetesClustersReconcileCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_scope_error_component import (
        ApiV1KubernetesClustersReconcileCreateScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_sla_availability_error_component import (
        ApiV1KubernetesClustersReconcileCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_sla_target_error_component import (
        ApiV1KubernetesClustersReconcileCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_slo_availability_error_component import (
        ApiV1KubernetesClustersReconcileCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_slo_target_error_component import (
        ApiV1KubernetesClustersReconcileCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_slug_error_component import (
        ApiV1KubernetesClustersReconcileCreateSlugErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_reconcile_create_target_availability_error_component import (
        ApiV1KubernetesClustersReconcileCreateTargetAvailabilityErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesClustersReconcileCreateValidationError")


@_attrs_define
class ApiV1KubernetesClustersReconcileCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesClustersReconcileCreateActiveErrorComponent |
            ApiV1KubernetesClustersReconcileCreateActualAvailabilityErrorComponent |
            ApiV1KubernetesClustersReconcileCreateAddonsErrorComponent |
            ApiV1KubernetesClustersReconcileCreateAliasErrorComponent |
            ApiV1KubernetesClustersReconcileCreateAnnotationsErrorComponent |
            ApiV1KubernetesClustersReconcileCreateApiServerCertExpiryDateErrorComponent |
            ApiV1KubernetesClustersReconcileCreateArchivedAtErrorComponent |
            ApiV1KubernetesClustersReconcileCreateArchivedErrorComponent |
            ApiV1KubernetesClustersReconcileCreateArchivedReasonErrorComponent |
            ApiV1KubernetesClustersReconcileCreateBackupSchedulesErrorComponent |
            ApiV1KubernetesClustersReconcileCreateBaserowIdErrorComponent |
            ApiV1KubernetesClustersReconcileCreateCredentialErrorComponent |
            ApiV1KubernetesClustersReconcileCreateCriticalityErrorComponent |
            ApiV1KubernetesClustersReconcileCreateDebugModeErrorComponent |
            ApiV1KubernetesClustersReconcileCreateDescriptionErrorComponent |
            ApiV1KubernetesClustersReconcileCreateDiscoveryEnabledErrorComponent |
            ApiV1KubernetesClustersReconcileCreateDiscoveryIgnoredNamespacesErrorComponent |
            ApiV1KubernetesClustersReconcileCreateDisplayNameErrorComponent |
            ApiV1KubernetesClustersReconcileCreateGitlabProjectIdErrorComponent |
            ApiV1KubernetesClustersReconcileCreateInstalledErrorComponent |
            ApiV1KubernetesClustersReconcileCreateIsHostClusterErrorComponent |
            ApiV1KubernetesClustersReconcileCreateIsInfrastructureClusterErrorComponent |
            ApiV1KubernetesClustersReconcileCreateKindErrorComponent |
            ApiV1KubernetesClustersReconcileCreateKubeconfigCaCertExpiryDateErrorComponent |
            ApiV1KubernetesClustersReconcileCreateKubeconfigClientCertExpiryDateErrorComponent |
            ApiV1KubernetesClustersReconcileCreateKubernetesVersionErrorComponent |
            ApiV1KubernetesClustersReconcileCreateLabelsErrorComponent |
            ApiV1KubernetesClustersReconcileCreateLastBackupImportErrorComponent |
            ApiV1KubernetesClustersReconcileCreateManagedByContentTypeErrorComponent |
            ApiV1KubernetesClustersReconcileCreateManagedByObjectIdErrorComponent |
            ApiV1KubernetesClustersReconcileCreateNameErrorComponent |
            ApiV1KubernetesClustersReconcileCreateNonFieldErrorsErrorComponent |
            ApiV1KubernetesClustersReconcileCreateOperatorIgnoreNamespacesErrorComponent |
            ApiV1KubernetesClustersReconcileCreateOperatorLoglevelErrorComponent |
            ApiV1KubernetesClustersReconcileCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1KubernetesClustersReconcileCreatePlatformServiceErrorComponent |
            ApiV1KubernetesClustersReconcileCreateProviderErrorComponent |
            ApiV1KubernetesClustersReconcileCreateProviderIdErrorComponent |
            ApiV1KubernetesClustersReconcileCreateProviderReferenceErrorComponent |
            ApiV1KubernetesClustersReconcileCreateReconciliationEnabledErrorComponent |
            ApiV1KubernetesClustersReconcileCreateScopeErrorComponent |
            ApiV1KubernetesClustersReconcileCreateSlaAvailabilityErrorComponent |
            ApiV1KubernetesClustersReconcileCreateSlaTargetErrorComponent |
            ApiV1KubernetesClustersReconcileCreateSloAvailabilityErrorComponent |
            ApiV1KubernetesClustersReconcileCreateSloTargetErrorComponent |
            ApiV1KubernetesClustersReconcileCreateSlugErrorComponent |
            ApiV1KubernetesClustersReconcileCreateTargetAvailabilityErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesClustersReconcileCreateActiveErrorComponent
        | ApiV1KubernetesClustersReconcileCreateActualAvailabilityErrorComponent
        | ApiV1KubernetesClustersReconcileCreateAddonsErrorComponent
        | ApiV1KubernetesClustersReconcileCreateAliasErrorComponent
        | ApiV1KubernetesClustersReconcileCreateAnnotationsErrorComponent
        | ApiV1KubernetesClustersReconcileCreateApiServerCertExpiryDateErrorComponent
        | ApiV1KubernetesClustersReconcileCreateArchivedAtErrorComponent
        | ApiV1KubernetesClustersReconcileCreateArchivedErrorComponent
        | ApiV1KubernetesClustersReconcileCreateArchivedReasonErrorComponent
        | ApiV1KubernetesClustersReconcileCreateBackupSchedulesErrorComponent
        | ApiV1KubernetesClustersReconcileCreateBaserowIdErrorComponent
        | ApiV1KubernetesClustersReconcileCreateCredentialErrorComponent
        | ApiV1KubernetesClustersReconcileCreateCriticalityErrorComponent
        | ApiV1KubernetesClustersReconcileCreateDebugModeErrorComponent
        | ApiV1KubernetesClustersReconcileCreateDescriptionErrorComponent
        | ApiV1KubernetesClustersReconcileCreateDiscoveryEnabledErrorComponent
        | ApiV1KubernetesClustersReconcileCreateDiscoveryIgnoredNamespacesErrorComponent
        | ApiV1KubernetesClustersReconcileCreateDisplayNameErrorComponent
        | ApiV1KubernetesClustersReconcileCreateGitlabProjectIdErrorComponent
        | ApiV1KubernetesClustersReconcileCreateInstalledErrorComponent
        | ApiV1KubernetesClustersReconcileCreateIsHostClusterErrorComponent
        | ApiV1KubernetesClustersReconcileCreateIsInfrastructureClusterErrorComponent
        | ApiV1KubernetesClustersReconcileCreateKindErrorComponent
        | ApiV1KubernetesClustersReconcileCreateKubeconfigCaCertExpiryDateErrorComponent
        | ApiV1KubernetesClustersReconcileCreateKubeconfigClientCertExpiryDateErrorComponent
        | ApiV1KubernetesClustersReconcileCreateKubernetesVersionErrorComponent
        | ApiV1KubernetesClustersReconcileCreateLabelsErrorComponent
        | ApiV1KubernetesClustersReconcileCreateLastBackupImportErrorComponent
        | ApiV1KubernetesClustersReconcileCreateManagedByContentTypeErrorComponent
        | ApiV1KubernetesClustersReconcileCreateManagedByObjectIdErrorComponent
        | ApiV1KubernetesClustersReconcileCreateNameErrorComponent
        | ApiV1KubernetesClustersReconcileCreateNonFieldErrorsErrorComponent
        | ApiV1KubernetesClustersReconcileCreateOperatorIgnoreNamespacesErrorComponent
        | ApiV1KubernetesClustersReconcileCreateOperatorLoglevelErrorComponent
        | ApiV1KubernetesClustersReconcileCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1KubernetesClustersReconcileCreatePlatformServiceErrorComponent
        | ApiV1KubernetesClustersReconcileCreateProviderErrorComponent
        | ApiV1KubernetesClustersReconcileCreateProviderIdErrorComponent
        | ApiV1KubernetesClustersReconcileCreateProviderReferenceErrorComponent
        | ApiV1KubernetesClustersReconcileCreateReconciliationEnabledErrorComponent
        | ApiV1KubernetesClustersReconcileCreateScopeErrorComponent
        | ApiV1KubernetesClustersReconcileCreateSlaAvailabilityErrorComponent
        | ApiV1KubernetesClustersReconcileCreateSlaTargetErrorComponent
        | ApiV1KubernetesClustersReconcileCreateSloAvailabilityErrorComponent
        | ApiV1KubernetesClustersReconcileCreateSloTargetErrorComponent
        | ApiV1KubernetesClustersReconcileCreateSlugErrorComponent
        | ApiV1KubernetesClustersReconcileCreateTargetAvailabilityErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_clusters_reconcile_create_active_error_component import (
            ApiV1KubernetesClustersReconcileCreateActiveErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_actual_availability_error_component import (
            ApiV1KubernetesClustersReconcileCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_addons_error_component import (
            ApiV1KubernetesClustersReconcileCreateAddonsErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_alias_error_component import (
            ApiV1KubernetesClustersReconcileCreateAliasErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_annotations_error_component import (
            ApiV1KubernetesClustersReconcileCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_api_server_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersReconcileCreateApiServerCertExpiryDateErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_archived_at_error_component import (
            ApiV1KubernetesClustersReconcileCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_archived_error_component import (
            ApiV1KubernetesClustersReconcileCreateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_archived_reason_error_component import (
            ApiV1KubernetesClustersReconcileCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_backup_schedules_error_component import (
            ApiV1KubernetesClustersReconcileCreateBackupSchedulesErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_baserow_id_error_component import (
            ApiV1KubernetesClustersReconcileCreateBaserowIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_credential_error_component import (
            ApiV1KubernetesClustersReconcileCreateCredentialErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_criticality_error_component import (
            ApiV1KubernetesClustersReconcileCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_debug_mode_error_component import (
            ApiV1KubernetesClustersReconcileCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_description_error_component import (
            ApiV1KubernetesClustersReconcileCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_discovery_enabled_error_component import (
            ApiV1KubernetesClustersReconcileCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_discovery_ignored_namespaces_error_component import (
            ApiV1KubernetesClustersReconcileCreateDiscoveryIgnoredNamespacesErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_display_name_error_component import (
            ApiV1KubernetesClustersReconcileCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_gitlab_project_id_error_component import (
            ApiV1KubernetesClustersReconcileCreateGitlabProjectIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_installed_error_component import (
            ApiV1KubernetesClustersReconcileCreateInstalledErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_is_host_cluster_error_component import (
            ApiV1KubernetesClustersReconcileCreateIsHostClusterErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_is_infrastructure_cluster_error_component import (
            ApiV1KubernetesClustersReconcileCreateIsInfrastructureClusterErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_kind_error_component import (
            ApiV1KubernetesClustersReconcileCreateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_kubeconfig_ca_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersReconcileCreateKubeconfigCaCertExpiryDateErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_kubeconfig_client_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersReconcileCreateKubeconfigClientCertExpiryDateErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_kubernetes_version_error_component import (
            ApiV1KubernetesClustersReconcileCreateKubernetesVersionErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_labels_error_component import (
            ApiV1KubernetesClustersReconcileCreateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_last_backup_import_error_component import (
            ApiV1KubernetesClustersReconcileCreateLastBackupImportErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_managed_by_content_type_error_component import (
            ApiV1KubernetesClustersReconcileCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_name_error_component import (
            ApiV1KubernetesClustersReconcileCreateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_non_field_errors_error_component import (
            ApiV1KubernetesClustersReconcileCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_operator_ignore_namespaces_error_component import (
            ApiV1KubernetesClustersReconcileCreateOperatorIgnoreNamespacesErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_operator_loglevel_error_component import (
            ApiV1KubernetesClustersReconcileCreateOperatorLoglevelErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_platform_dns_record_created_error_component import (
            ApiV1KubernetesClustersReconcileCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_platform_service_error_component import (
            ApiV1KubernetesClustersReconcileCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_provider_error_component import (
            ApiV1KubernetesClustersReconcileCreateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_provider_id_error_component import (
            ApiV1KubernetesClustersReconcileCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_provider_reference_error_component import (
            ApiV1KubernetesClustersReconcileCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesClustersReconcileCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_scope_error_component import (
            ApiV1KubernetesClustersReconcileCreateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_sla_availability_error_component import (
            ApiV1KubernetesClustersReconcileCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_sla_target_error_component import (
            ApiV1KubernetesClustersReconcileCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_slo_availability_error_component import (
            ApiV1KubernetesClustersReconcileCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_slo_target_error_component import (
            ApiV1KubernetesClustersReconcileCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_slug_error_component import (
            ApiV1KubernetesClustersReconcileCreateSlugErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_target_availability_error_component import (
            ApiV1KubernetesClustersReconcileCreateTargetAvailabilityErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesClustersReconcileCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersReconcileCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersReconcileCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersReconcileCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersReconcileCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersReconcileCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersReconcileCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersReconcileCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersReconcileCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersReconcileCreateReconciliationEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersReconcileCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersReconcileCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersReconcileCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersReconcileCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersReconcileCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersReconcileCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersReconcileCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersReconcileCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersReconcileCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersReconcileCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersReconcileCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersReconcileCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersReconcileCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersReconcileCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersReconcileCreateKubernetesVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersReconcileCreateInstalledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersReconcileCreateIsHostClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersReconcileCreateIsInfrastructureClusterErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersReconcileCreateKubeconfigCaCertExpiryDateErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersReconcileCreateKubeconfigClientCertExpiryDateErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersReconcileCreateApiServerCertExpiryDateErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersReconcileCreateCredentialErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersReconcileCreateDiscoveryIgnoredNamespacesErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersReconcileCreateOperatorLoglevelErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersReconcileCreateOperatorIgnoreNamespacesErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersReconcileCreateAliasErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersReconcileCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersReconcileCreateAddonsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersReconcileCreateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersReconcileCreateBackupSchedulesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersReconcileCreateBaserowIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersReconcileCreateGitlabProjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersReconcileCreateLastBackupImportErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersReconcileCreatePlatformDnsRecordCreatedErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersReconcileCreateSlugErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersReconcileCreateManagedByContentTypeErrorComponent):
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
        from ..models.api_v1_kubernetes_clusters_reconcile_create_active_error_component import (
            ApiV1KubernetesClustersReconcileCreateActiveErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_actual_availability_error_component import (
            ApiV1KubernetesClustersReconcileCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_addons_error_component import (
            ApiV1KubernetesClustersReconcileCreateAddonsErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_alias_error_component import (
            ApiV1KubernetesClustersReconcileCreateAliasErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_annotations_error_component import (
            ApiV1KubernetesClustersReconcileCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_api_server_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersReconcileCreateApiServerCertExpiryDateErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_archived_at_error_component import (
            ApiV1KubernetesClustersReconcileCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_archived_error_component import (
            ApiV1KubernetesClustersReconcileCreateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_archived_reason_error_component import (
            ApiV1KubernetesClustersReconcileCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_backup_schedules_error_component import (
            ApiV1KubernetesClustersReconcileCreateBackupSchedulesErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_baserow_id_error_component import (
            ApiV1KubernetesClustersReconcileCreateBaserowIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_credential_error_component import (
            ApiV1KubernetesClustersReconcileCreateCredentialErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_criticality_error_component import (
            ApiV1KubernetesClustersReconcileCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_debug_mode_error_component import (
            ApiV1KubernetesClustersReconcileCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_description_error_component import (
            ApiV1KubernetesClustersReconcileCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_discovery_enabled_error_component import (
            ApiV1KubernetesClustersReconcileCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_discovery_ignored_namespaces_error_component import (
            ApiV1KubernetesClustersReconcileCreateDiscoveryIgnoredNamespacesErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_display_name_error_component import (
            ApiV1KubernetesClustersReconcileCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_gitlab_project_id_error_component import (
            ApiV1KubernetesClustersReconcileCreateGitlabProjectIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_installed_error_component import (
            ApiV1KubernetesClustersReconcileCreateInstalledErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_is_host_cluster_error_component import (
            ApiV1KubernetesClustersReconcileCreateIsHostClusterErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_is_infrastructure_cluster_error_component import (
            ApiV1KubernetesClustersReconcileCreateIsInfrastructureClusterErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_kind_error_component import (
            ApiV1KubernetesClustersReconcileCreateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_kubeconfig_ca_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersReconcileCreateKubeconfigCaCertExpiryDateErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_kubeconfig_client_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersReconcileCreateKubeconfigClientCertExpiryDateErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_kubernetes_version_error_component import (
            ApiV1KubernetesClustersReconcileCreateKubernetesVersionErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_labels_error_component import (
            ApiV1KubernetesClustersReconcileCreateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_last_backup_import_error_component import (
            ApiV1KubernetesClustersReconcileCreateLastBackupImportErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_managed_by_content_type_error_component import (
            ApiV1KubernetesClustersReconcileCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_managed_by_object_id_error_component import (
            ApiV1KubernetesClustersReconcileCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_name_error_component import (
            ApiV1KubernetesClustersReconcileCreateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_non_field_errors_error_component import (
            ApiV1KubernetesClustersReconcileCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_operator_ignore_namespaces_error_component import (
            ApiV1KubernetesClustersReconcileCreateOperatorIgnoreNamespacesErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_operator_loglevel_error_component import (
            ApiV1KubernetesClustersReconcileCreateOperatorLoglevelErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_platform_dns_record_created_error_component import (
            ApiV1KubernetesClustersReconcileCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_platform_service_error_component import (
            ApiV1KubernetesClustersReconcileCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_provider_error_component import (
            ApiV1KubernetesClustersReconcileCreateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_provider_id_error_component import (
            ApiV1KubernetesClustersReconcileCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_provider_reference_error_component import (
            ApiV1KubernetesClustersReconcileCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesClustersReconcileCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_scope_error_component import (
            ApiV1KubernetesClustersReconcileCreateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_sla_availability_error_component import (
            ApiV1KubernetesClustersReconcileCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_sla_target_error_component import (
            ApiV1KubernetesClustersReconcileCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_slo_availability_error_component import (
            ApiV1KubernetesClustersReconcileCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_slo_target_error_component import (
            ApiV1KubernetesClustersReconcileCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_slug_error_component import (
            ApiV1KubernetesClustersReconcileCreateSlugErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_reconcile_create_target_availability_error_component import (
            ApiV1KubernetesClustersReconcileCreateTargetAvailabilityErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesClustersReconcileCreateActiveErrorComponent
                | ApiV1KubernetesClustersReconcileCreateActualAvailabilityErrorComponent
                | ApiV1KubernetesClustersReconcileCreateAddonsErrorComponent
                | ApiV1KubernetesClustersReconcileCreateAliasErrorComponent
                | ApiV1KubernetesClustersReconcileCreateAnnotationsErrorComponent
                | ApiV1KubernetesClustersReconcileCreateApiServerCertExpiryDateErrorComponent
                | ApiV1KubernetesClustersReconcileCreateArchivedAtErrorComponent
                | ApiV1KubernetesClustersReconcileCreateArchivedErrorComponent
                | ApiV1KubernetesClustersReconcileCreateArchivedReasonErrorComponent
                | ApiV1KubernetesClustersReconcileCreateBackupSchedulesErrorComponent
                | ApiV1KubernetesClustersReconcileCreateBaserowIdErrorComponent
                | ApiV1KubernetesClustersReconcileCreateCredentialErrorComponent
                | ApiV1KubernetesClustersReconcileCreateCriticalityErrorComponent
                | ApiV1KubernetesClustersReconcileCreateDebugModeErrorComponent
                | ApiV1KubernetesClustersReconcileCreateDescriptionErrorComponent
                | ApiV1KubernetesClustersReconcileCreateDiscoveryEnabledErrorComponent
                | ApiV1KubernetesClustersReconcileCreateDiscoveryIgnoredNamespacesErrorComponent
                | ApiV1KubernetesClustersReconcileCreateDisplayNameErrorComponent
                | ApiV1KubernetesClustersReconcileCreateGitlabProjectIdErrorComponent
                | ApiV1KubernetesClustersReconcileCreateInstalledErrorComponent
                | ApiV1KubernetesClustersReconcileCreateIsHostClusterErrorComponent
                | ApiV1KubernetesClustersReconcileCreateIsInfrastructureClusterErrorComponent
                | ApiV1KubernetesClustersReconcileCreateKindErrorComponent
                | ApiV1KubernetesClustersReconcileCreateKubeconfigCaCertExpiryDateErrorComponent
                | ApiV1KubernetesClustersReconcileCreateKubeconfigClientCertExpiryDateErrorComponent
                | ApiV1KubernetesClustersReconcileCreateKubernetesVersionErrorComponent
                | ApiV1KubernetesClustersReconcileCreateLabelsErrorComponent
                | ApiV1KubernetesClustersReconcileCreateLastBackupImportErrorComponent
                | ApiV1KubernetesClustersReconcileCreateManagedByContentTypeErrorComponent
                | ApiV1KubernetesClustersReconcileCreateManagedByObjectIdErrorComponent
                | ApiV1KubernetesClustersReconcileCreateNameErrorComponent
                | ApiV1KubernetesClustersReconcileCreateNonFieldErrorsErrorComponent
                | ApiV1KubernetesClustersReconcileCreateOperatorIgnoreNamespacesErrorComponent
                | ApiV1KubernetesClustersReconcileCreateOperatorLoglevelErrorComponent
                | ApiV1KubernetesClustersReconcileCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1KubernetesClustersReconcileCreatePlatformServiceErrorComponent
                | ApiV1KubernetesClustersReconcileCreateProviderErrorComponent
                | ApiV1KubernetesClustersReconcileCreateProviderIdErrorComponent
                | ApiV1KubernetesClustersReconcileCreateProviderReferenceErrorComponent
                | ApiV1KubernetesClustersReconcileCreateReconciliationEnabledErrorComponent
                | ApiV1KubernetesClustersReconcileCreateScopeErrorComponent
                | ApiV1KubernetesClustersReconcileCreateSlaAvailabilityErrorComponent
                | ApiV1KubernetesClustersReconcileCreateSlaTargetErrorComponent
                | ApiV1KubernetesClustersReconcileCreateSloAvailabilityErrorComponent
                | ApiV1KubernetesClustersReconcileCreateSloTargetErrorComponent
                | ApiV1KubernetesClustersReconcileCreateSlugErrorComponent
                | ApiV1KubernetesClustersReconcileCreateTargetAvailabilityErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_0 = (
                        ApiV1KubernetesClustersReconcileCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_1 = (
                        ApiV1KubernetesClustersReconcileCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_2 = (
                        ApiV1KubernetesClustersReconcileCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_3 = (
                        ApiV1KubernetesClustersReconcileCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_4 = (
                        ApiV1KubernetesClustersReconcileCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_5 = (
                        ApiV1KubernetesClustersReconcileCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_6 = (
                        ApiV1KubernetesClustersReconcileCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_7 = (
                        ApiV1KubernetesClustersReconcileCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_8 = (
                        ApiV1KubernetesClustersReconcileCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_9 = (
                        ApiV1KubernetesClustersReconcileCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_10 = (
                        ApiV1KubernetesClustersReconcileCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_11 = (
                        ApiV1KubernetesClustersReconcileCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_12 = (
                        ApiV1KubernetesClustersReconcileCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_13 = (
                        ApiV1KubernetesClustersReconcileCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_14 = (
                        ApiV1KubernetesClustersReconcileCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_15 = (
                        ApiV1KubernetesClustersReconcileCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_16 = (
                        ApiV1KubernetesClustersReconcileCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_17 = (
                        ApiV1KubernetesClustersReconcileCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_18 = (
                        ApiV1KubernetesClustersReconcileCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_19 = (
                        ApiV1KubernetesClustersReconcileCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_20 = (
                        ApiV1KubernetesClustersReconcileCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_21 = (
                        ApiV1KubernetesClustersReconcileCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_22 = (
                        ApiV1KubernetesClustersReconcileCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_23 = (
                        ApiV1KubernetesClustersReconcileCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_24 = (
                        ApiV1KubernetesClustersReconcileCreateKubernetesVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_25 = (
                        ApiV1KubernetesClustersReconcileCreateInstalledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_26 = (
                        ApiV1KubernetesClustersReconcileCreateIsHostClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_27 = (
                        ApiV1KubernetesClustersReconcileCreateIsInfrastructureClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_28 = (
                        ApiV1KubernetesClustersReconcileCreateKubeconfigCaCertExpiryDateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_29 = (
                        ApiV1KubernetesClustersReconcileCreateKubeconfigClientCertExpiryDateErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_30 = (
                        ApiV1KubernetesClustersReconcileCreateApiServerCertExpiryDateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_31 = (
                        ApiV1KubernetesClustersReconcileCreateCredentialErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_32 = (
                        ApiV1KubernetesClustersReconcileCreateDiscoveryIgnoredNamespacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_33 = (
                        ApiV1KubernetesClustersReconcileCreateOperatorLoglevelErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_34 = (
                        ApiV1KubernetesClustersReconcileCreateOperatorIgnoreNamespacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_35 = (
                        ApiV1KubernetesClustersReconcileCreateAliasErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_36 = (
                        ApiV1KubernetesClustersReconcileCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_37 = (
                        ApiV1KubernetesClustersReconcileCreateAddonsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_38 = (
                        ApiV1KubernetesClustersReconcileCreateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_39 = (
                        ApiV1KubernetesClustersReconcileCreateBackupSchedulesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_40 = (
                        ApiV1KubernetesClustersReconcileCreateBaserowIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_41 = (
                        ApiV1KubernetesClustersReconcileCreateGitlabProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_42 = (
                        ApiV1KubernetesClustersReconcileCreateLastBackupImportErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_43 = (
                        ApiV1KubernetesClustersReconcileCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_44 = (
                        ApiV1KubernetesClustersReconcileCreateSlugErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_45 = (
                        ApiV1KubernetesClustersReconcileCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_46 = (
                    ApiV1KubernetesClustersReconcileCreateManagedByObjectIdErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_clusters_reconcile_create_error_type_46

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_clusters_reconcile_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_clusters_reconcile_create_validation_error.additional_properties = d
        return api_v1_kubernetes_clusters_reconcile_create_validation_error

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
